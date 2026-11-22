# Testing report

| Check | Observed result |
| --- | --- |
| Dataset inventory | 1,095 distinct days, seven locations, no missing cells. Original and delivered CSV checksums match. |
| Original training | Linear Regression R² 0.9914, MAE 7.93, RMSE 10.35. Random Forest classifier accuracy 94.52%. |
| Corrected training | Same headline regression metrics. Selected Logistic Regression accuracy 94.06% on 219 holdout rows; Random Forest holdout accuracy 94.52%. |
| Flask automated suite | 9 passed. All five endpoints, validation and CORS, AQI boundaries, budget tiers, artifact metadata and train-only scaling. |
| React automated suite | 6 passed. Dashboard, retry, blank and preset prediction, prediction loading and error, forecast and insights. |
| Live browser check | Dashboard fetched historical data and drew charts, Winter predicted AQI 344.6, simulation returned seven days and drew a chart, insights displayed coefficients and 94.06% accuracy. The mobile Dashboard fit a 390px viewport. |
| Production build | Vite completed successfully. It reported a JavaScript chunk above 500 kB before compression. |
| Remote CI | Pending confirmed repository, GitHub identity and push. |
| Deployment | Hosting configuration supplied. No deployment workflow or live deployment was run. |

The live check used local Vite and Waitress on loopback port 8787 for Flask. The environment did not connect to the Flask development server on port 5000. The Vitest suite uses a mock API and stubs responsive chart containers. The live browser check exercised the actual API and chart rendering.
