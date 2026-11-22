# Initial project audit

The supplied archive contains a React/Vite SPA and a Flask API. The client uses React Router, Recharts, Tailwind and a fetch wrapper. The API scales ordered numeric features, calls two serialized estimators, and serves pandas aggregates from the original CSV.

## Archive inventory

- Root contains README.md.
- backend contains app.py, train.py, requirements.txt and data/delhi_aqi_data.csv.
- frontend contains package.json, index.html, vite.config.js, tailwind.config.js and postcss.config.js.
- frontend/src contains main.jsx, App.jsx, index.css, hooks/useApi.js, services/api.js and utils/aqi.js.
- frontend/src/pages contains Dashboard.jsx, Predict.jsx, Forecast.jsx and ModelInsights.jsx.
- frontend/src/components contains AqiGauge, CustomTooltip, ErrorCard, PageHeader, Sidebar, Spinner and StatCard JSX components.
- Two brace-expression directory names are empty archive artifacts. No Git metadata, tests, workflows, lockfile or fitted models are supplied.

## Observed baseline

| Capability | Source inspection |
| --- | --- |
| Health and startup | Health handler exists. Import requires absent artifacts. Development launch enables debug. |
| Predict and budget | Handler, form, three presets, gauge, probabilities, budget and graded recommendations exist. Missing values silently become zero. Decimal AQI falls between category bounds. Error responses can disclose exception details. |
| Dashboard | Historical trend, monthly, station and risk charts exist. The synopsis specifies 60 days and the source takes 60 observations. These are equivalent for this CSV. The dashboard lacks explicit budget statistics. |
| Forecast | Seven baseline perturbations are implemented. The month control is read but ignored. Invalid JSON and out-of-range values are inadequately handled. |
| Model insights | Comparisons, feature list and confusion matrix exist. Linear winner interpretation is absent. UI infers winners from rounded evaluation scores. |
| Dataset and ML | The original CSV has 1,095 unique dates, 7 locations and no missing cells. Dates span 2022-01-01 to 2024-12-30. Mean AQI is 196.539 and risk counts are 236/411/448. Training fits scaling before splitting and selects on the test set. Historical metrics are recorded in the synopsis and require reproduction. |
| Responsive layout | Content grids adapt but the fixed-width sidebar occupies much of the mobile viewport. Footer names the wrong semester. |
| Testing and hosting | No automated tests, CI or deployment setup. Wildcard CORS and a loopback production fallback require configuration changes. |

The PDF is the requirements reference. Its reported test outcomes are historical claims and were not observed in this initial audit. Local execution requires dependencies and regenerated artifacts.

## Prioritized backlog

1. Correct evaluation isolation and expose reproducible metrics and interpretation.
2. Validate the API and prediction form, and make budget boundaries consistent.
3. Correct and label the forecast simulation and expose dashboard budget data.
4. Test routes and UI states, pin dependency resolution, and add CI.
5. Record actual sprint evidence and configure deployment after targets are established.
