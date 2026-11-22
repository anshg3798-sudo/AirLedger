# Architecture

The browser routes four pages through App.jsx and fetches JSON through services/api.js. Dashboard and Model Insights use the useApi hook for loading, error and retry states. Predict and Forecast own their form and result state.

Flask routes validate JSON using schema.py. Predict derives the weekend field, constructs a pandas frame in the training feature order and invokes both pipelines. The API applies the six AQI bands, the fixed budget and the recommendation tiers to the one-decimal AQI. Forecast generates seven bounded baseline variations, then scores all seven rows in one model call.

The dashboard groups the supplied CSV by date, month, location and risk. The model-info route returns metadata generated alongside the trained models. The artifact is replaced atomically after training and loaded once per API process. Artifacts belong to the local or deployment environment.

The split is 876/219, seed 42. Training-only cross-validation ranks candidate pipelines. The holdout produces comparison scores and a fixed-label confusion matrix. Coefficients express predicted AQI change per one training standard deviation, holding the other standardized inputs fixed.
