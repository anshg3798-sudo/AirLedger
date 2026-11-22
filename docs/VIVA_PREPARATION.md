# Viva preparation

**What problem does AirLedger solve?** It turns environmental inputs into an AQI estimate, compares it with a budget of 100 and lists graded actions.

**What happens after pressing Predict?** Predict.jsx calls services/api.js, which sends JSON to Flask. schema.py validates input and derives the weekend flag. app.py scores both fitted pipelines and returns the AQI, category, risk, probabilities, budget and actions.

**Why split the data before fitting the scaler?** A fitted scaler learns means and standard deviations. Learning them from test rows leaks information into training. Each candidate fits preprocessing inside its training folds and reports metrics on a holdout that did not select the winner.

**Why did the selected classifier change?** Logistic Regression won the training-fold comparison. The original selection used the holdout, where Random Forest had the higher score. The corrected pipeline still reports both scores.

**What does the confusion matrix show?** Rows show actual classes and columns show predictions. Diagonal counts are correct classifications. Nearby off-diagonal counts show confusion between adjacent risk classes.

**How does the forecast work?** Each day perturbs user baseline inputs and runs the same models using that date's calendar features. It illustrates a scenario.

**How does the project show Agile development?** Each sprint has a user story, acceptance criteria, implementation paths and test evidence. After a Git remote is confirmed, use genuine commit diffs and CI runs as additional evidence. Commits preserve changes, and CI repeats the verification on fresh runners.
