# AirLedger – AI-Driven Pollution Budgeting for Delhi-NCR

AirLedger lets users explore how changes in pollutant concentrations, weather and calendar inputs affect estimated AQI in Delhi-NCR. It quantifies overshoot above AQI 100 and provides graded, illustrative response options.

## Application

| Page | What it provides |
| --- | --- |
| Dashboard | Historical KPIs, days over budget, 60 observation dates, monthly and location averages, and risk distribution |
| Predict AQI | Twelve editable inputs, derived weekend indicator, seasonal presets, AQI gauge, risk probabilities, budget and recommendations |
| Seven-Day Forecast | Simulated future AQI, categories and risks based on perturbed baseline conditions |
| Model Insights | Selected models, holdout metrics, comparisons, confusion matrix and standardized regression coefficients |

React, Vite, React Router, Tailwind and Recharts power the client. Flask and Flask-CORS serve JSON. pandas, NumPy, scikit-learn and joblib power training, analytics and inference.

```text
React SPA → fetch /api → Flask → serialized scikit-learn pipelines
                             ↳ CSV → dashboard aggregates
```

## Run locally

Use Python 3.12 and Node.js 22.12 or newer. From the project root in PowerShell:

```powershell
py -3.12 -m venv .venv
cd backend
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
..\.venv\Scripts\python.exe train.py
..\.venv\Scripts\python.exe app.py
```

In a second terminal at the project root:

```powershell
cd frontend
npm ci
npm run dev
```

Open http://localhost:5173. Vite forwards API calls to Flask on port 5000. For macOS, Linux and other configurations, see [Setup](docs/SETUP_GUIDE.md).

## Training and validation

The supplied CSV has 1,095 records across seven locations. Training drops incomplete model rows, holds out 219 records with seed 42 and selects candidates using five folds within the remaining 876. Each model pipeline fits a StandardScaler using its own training rows. Running `train.py` writes the model bundle locally. Restart the backend after retraining.

| Metric | Synopsis and reproduced original pipeline | Delivered pipeline |
| --- | --- | --- |
| Selected regressor | Linear Regression | Linear Regression |
| R² | 0.9914 | 0.9914 |
| MAE | 7.93 | 7.93 |
| RMSE | 10.35 | 10.35 |
| Selected classifier | Random Forest | Logistic Regression |
| Holdout accuracy | 94.52% | 94.06% |

Logistic Regression scored 93.15% in training cross-validation, compared with 92.69% for Random Forest. Random Forest still scored 94.52% on the holdout. The original script selected using that holdout and scaled the full dataset before splitting.

From `backend/`, run `python -m unittest discover -s tests -v` after training. From `frontend/`, run `npm test` and `npm run build`.

## API and repository

Requests and JSON examples are in the [API reference](docs/API_DOCUMENTATION.md).

| Method | Endpoint |
| --- | --- |
| GET | `/api/health` |
| POST | `/api/predict` |
| GET | `/api/dashboard` |
| GET | `/api/model-info` |
| POST | `/api/forecast` |

- `backend/` contains the Flask app, feature schema, CSV, model training, API tests and Dockerfile.
- `frontend/` contains React pages, components, hooks, API client, Vitest checks and Vercel routing.
- `agile/` maps user stories to five verified development increments.
- `docs/` contains the audit, architecture, setup, API, testing, CI/CD, deployment, demo and viva guides.
- `.github/workflows/` contains Python training and test CI plus a lockfile-based frontend test and build workflow.

The five sprints cover [models](agile/SPRINT_1.md), [prediction](agile/SPRINT_2.md), [budget](agile/SPRINT_3.md), [dashboard and simulation](agile/SPRINT_4.md), and [model insights and verification](agile/SPRINT_5.md). See the [product backlog](agile/PRODUCT_BACKLOG.md) and [testing report](agile/TESTING_REPORT.md) for evidence.

GitHub Actions workflows run on pushes to main, pull requests targeting main and manual dispatch. See the [CI/CD guide](docs/CI_CD_GUIDE.md) and [deployment guide](docs/DEPLOYMENT_GUIDE.md) for Vercel and a container-based Flask host.

## Limitations and future scope

The CSV has one observation per date, with varying locations. Model features omit station identity. Risk labels derive from AQI bands, and a random holdout measures performance on this dataset. The seven-day outlook uses simulated inputs and no live weather feed. Recommendations illustrate graded responses for the lab. Future work could evaluate chronological and station-based splits, integrate station and weather feeds and validate a genuine forecasting model.

## Team

Fundamentals of Agile Development Lab, B.Tech CSE Semester 5, Jaypee Institute of Information Technology, Noida. Submitted to Prof. Sulabh Tyagi.

| Student | Enrollment | Batch |
| --- | --- | --- |
| Jaya Sharma | 992401030331 | F7 |
| Pulkeshin Goyal | 992401030333 | F7 |
| Ansh | 992401030341 | F7 |
| Shubhi Gupta | 992401030366 | F8 |
