import math
import unittest
from datetime import date, timedelta

from app import app, categorize_aqi, get_recommendations, models, pollution_budget
from schema import FEATURES
from train import DATA_PATH

WINTER = dict(pm25=180, pm10=270, no2=65, so2=30, co=3.5, temperature=14,
              humidity=78, wind_speed=2.5, rainfall=0, visibility=3, month=12, day_of_week=1)


class AirLedgerTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_and_cors(self):
        self.assertEqual(self.client.get("/api/health").json["status"], "ok")
        for origin, allowed in [("http://localhost:5173", True), ("https://untrusted.test", False)]:
            with self.subTest(origin=origin):
                result = self.client.options("/api/predict", headers={
                    "Origin": origin, "Access-Control-Request-Method": "POST",
                    "Access-Control-Request-Headers": "Content-Type",
                })
                self.assertEqual("Access-Control-Allow-Origin" in result.headers, allowed)

    def test_prediction_and_probability_labels(self):
        response = self.client.post("/api/predict", json=WINTER)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertGreater(data["aqi"], 300)
        self.assertEqual(data["category"], "Very Poor")
        self.assertEqual(data["risk_label"], "High Risk")
        self.assertEqual(set(data["risk_probabilities"]), {"Safe", "Moderate", "High Risk"})
        self.assertAlmostEqual(sum(data["risk_probabilities"].values()), 100, delta=0.15)
        self.assertEqual(data["pollution_budget"], pollution_budget(data["aqi"]))
        self.assertEqual(len(data["recommendations"]), 5)
        self.assertEqual(self.client.post("/api/predict", json={**WINTER, "is_weekend": 0}).json, data)

    def test_invalid_prediction(self):
        cases = [
            ({}, "pm25"), ({**WINTER, "pm25": "180"}, "pm25"), ({**WINTER, "pm25": math.nan}, "pm25"),
            ({**WINTER, "humidity": 101}, "humidity"), ({**WINTER, "pm10": True}, "pm10"),
            ({**WINTER, "month": 3.5}, "month"), ({**WINTER, "is_weekend": 1}, "is_weekend"),
            ([], "JSON object"),
        ]
        for payload, field in cases:
            with self.subTest(payload=payload):
                response = self.client.post("/api/predict", json=payload)
                self.assertEqual(response.status_code, 400)
                self.assertIn(field, response.json["error"])

    def test_json_protocol(self):
        for route in ["/api/predict", "/api/forecast"]:
            self.assertEqual(self.client.post(route, data="{}").status_code, 415)
            response = self.client.post(route, data="{", content_type="application/json")
            self.assertEqual(response.status_code, 400)
            self.assertIn("error", response.json)

    def test_categories(self):
        cases = [(0, "Good"), (50, "Good"), (50.1, "Satisfactory"), (100, "Satisfactory"),
                 (100.1, "Moderate"), (200, "Moderate"), (200.1, "Poor"), (300, "Poor"),
                 (300.1, "Very Poor"), (400, "Very Poor"), (400.1, "Severe"), (500, "Severe")]
        for aqi, category in cases:
            with self.subTest(aqi=aqi):
                self.assertEqual(categorize_aqi(aqi)[0], category)

    def test_budget_and_recommendation_tiers(self):
        for aqi, priority, count in [(100, "Info", 2), (100.1, "Low", 3), (200.1, "Medium", 4), (300.1, "High", 5)]:
            with self.subTest(aqi=aqi):
                budget = pollution_budget(aqi)
                self.assertEqual(budget["exceeded"], aqi > 100)
                self.assertAlmostEqual(budget["overshoot"], aqi - 100)
                actions = get_recommendations(aqi)
                self.assertEqual(len(actions), count)
                self.assertEqual({action["priority"] for action in actions}, {priority})

    def test_dashboard(self):
        response = self.client.get("/api/dashboard")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["stats"]["total_days"], 1095)
        self.assertEqual(data["stats"]["avg_aqi"], 196.5)
        self.assertEqual(len(data["trend"]), 60)
        self.assertEqual(len(data["monthly"]), 12)
        self.assertEqual(len(data["by_location"]), 7)
        self.assertEqual(sum(row["count"] for row in data["risk_dist"]), 1095)
        self.assertGreater(data["pollution_budget"]["observations_exceeded"], 0)

    def test_model_metadata_and_training_partition(self):
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from numpy.testing import assert_allclose

        response = self.client.get("/api/model-info")
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["features"], FEATURES)
        self.assertEqual(sum(map(sum, data["confusion_matrix"])), data["test_size"])
        train, _ = train_test_split(pd.read_csv(DATA_PATH), test_size=0.2, random_state=42)
        for key in ["regressor", "classifier"]:
            assert_allclose(models()[key].named_steps["standardscaler"].mean_, train[FEATURES].mean())
        self.assertGreaterEqual(data["regression"][data["selected_regressor"]]["r2"], 0.98)
        self.assertGreaterEqual(data["classification"][data["selected_classifier"]]["accuracy"], 0.90)
        self.assertEqual(set(data["coefficients"] or data["feature_importance"]), set(FEATURES))

    def test_forecast(self):
        response = self.client.post("/api/forecast", json={"base_pm25": 150})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["mode"], "simulation")
        forecasts = response.json["forecast"]
        self.assertEqual(len(forecasts), 7)
        dates = [date.fromisoformat(row["iso_date"]) for row in forecasts]
        self.assertEqual(dates, [dates[0] + timedelta(days=i) for i in range(7)])
        for row in forecasts:
            self.assertTrue(0 <= row["aqi"] <= 500)
            self.assertEqual(row["category"], categorize_aqi(row["aqi"])[0])
            self.assertIn(row["risk"], ["Safe", "Moderate", "High Risk"])
        self.assertEqual(self.client.post("/api/forecast", json={"base_humidity": 200}).status_code, 400)
