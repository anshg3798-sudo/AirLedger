# API reference

The local base URL is `http://127.0.0.1:5000`. POST requests require `Content-Type: application/json`. Errors contain a JSON `error` string. Invalid fields or malformed JSON return 400, other content types return 415, missing model artifacts return 503 on model-dependent routes and unexpected errors return a generic 500.

## GET /api/health

Returns `{"status":"ok","message":"AirLedger API running"}` when the artifact can be loaded.

## POST /api/predict

```json
{
  "pm25": 180, "pm10": 270, "no2": 65, "so2": 30, "co": 3.5,
  "temperature": 14, "humidity": 78, "wind_speed": 2.5, "rainfall": 0,
  "visibility": 3, "month": 12, "day_of_week": 1
}
```

All shown fields are required numeric JSON values. PM2.5, PM10, NO₂ and SO₂ are in μg/m³ with maximums 500, 600, 200 and 100. CO is 0–20 mg/m³. Temperature is −5–50 °C, humidity 0–100%, wind 0–60 km/h, rainfall 0–100 mm and visibility 0–25 km. Month is 1–12. Day of week is 0–6 with Monday at 0. The API derives the weekend flag. A supplied legacy `is_weekend` value must agree.

The response contains one-decimal `aqi`, `category` and `category_color`, `risk_level` (0–2), `risk_label`, `risk_color`, `risk_probabilities` in percent, `recommendations` with action/priority/icon fields and `pollution_budget` with limit, prediction, exceeded flag and overshoot.

Category upper bounds are 50, 100, 200, 300, 400 and 500. Recommendation tier changes occur above 100, 200 and 300. Risk is an independent classification result based on the same inputs.

## GET /api/dashboard

Returns `stats`, `trend` (up to 60 distinct dates), `monthly`, `by_location`, `risk_dist` and `pollution_budget`. Budget observations count actual AQI strictly above 100. Risk counts use the dataset's provided labels.

## GET /api/model-info

Returns selected model names, train/test sizes, model comparisons, coefficients or tree importance, feature names and the selected classifier's confusion matrix. Matrix rows are actual labels and columns are predictions in Safe, Moderate, High Risk order.

## POST /api/forecast

```json
{"base_pm25":80,"base_temp":25,"base_humidity":55,"base_wind":5}
```

The example values are the defaults. Limits are 0–400 μg/m³, −5–50 °C, 0–100% and 0–40 km/h. An optional integer `month` 1–12 overrides the month feature for legacy scenario clients. The seven dates still represent the following seven Delhi calendar days. The response includes `mode: "simulation"`, and each forecast entry contains ISO date, display date, AQI, category, risk and colors.
