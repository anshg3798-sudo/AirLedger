"""Train and evaluate AirLedger models on the supplied CSV."""
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import joblib
import pandas as pd
from sklearn.ensemble import (
    GradientBoostingRegressor,
    RandomForestClassifier,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from schema import FEATURES

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "delhi_aqi_data.csv"
MODEL_PATH = BASE_DIR / "model" / "airledger.joblib"
SEED = 42


def evaluate(candidates, X_train, X_test, y_train, y_test, cv, scoring, metrics):
    """Select by training-fold scores and report all candidates on the holdout."""
    pipelines = {name: make_pipeline(StandardScaler(), model) for name, model in candidates.items()}
    scores = {
        name: cross_val_score(model, X_train, y_train, cv=cv, scoring=scoring).mean()
        for name, model in pipelines.items()
    }
    selected = max(scores, key=scores.get)
    results = {}
    for name, model in pipelines.items():
        model.fit(X_train, y_train)
        results[name] = {
            **metrics(y_test, model.predict(X_test)),
            "cv_score": round(float(scores[name]), 4),
        }
    return selected, pipelines[selected], results


def regression_metrics(actual, predicted):
    return {
        "mae": round(mean_absolute_error(actual, predicted), 2),
        "rmse": round(mean_squared_error(actual, predicted) ** 0.5, 2),
        "r2": round(r2_score(actual, predicted), 4),
    }


def main():
    data = pd.read_csv(DATA_PATH).dropna(subset=[*FEATURES, "aqi", "risk_level"])
    train, test = train_test_split(data, test_size=0.2, random_state=SEED)
    X_train, X_test = train[FEATURES], test[FEATURES]
    reg_name, regressor, regression = evaluate(
        {
            "Linear Regression": LinearRegression(),
            "Random Forest": RandomForestRegressor(n_estimators=120, random_state=SEED),
            "Gradient Boosting": GradientBoostingRegressor(n_estimators=120, random_state=SEED),
        },
        X_train, X_test, train.aqi, test.aqi, KFold(5, shuffle=True, random_state=SEED),
        "r2", regression_metrics,
    )
    cls_name, classifier, classification = evaluate(
        {
            "Logistic Regression": LogisticRegression(max_iter=500, random_state=SEED),
            "Random Forest": RandomForestClassifier(n_estimators=120, random_state=SEED),
        },
        X_train, X_test, train.risk_level, test.risk_level,
        StratifiedKFold(5, shuffle=True, random_state=SEED),
        "accuracy", lambda actual, predicted: {"accuracy": round(accuracy_score(actual, predicted), 4)},
    )
    estimator = regressor.steps[-1][1]
    importance = getattr(estimator, "feature_importances_", [])
    coefficients = getattr(estimator, "coef_", [])
    meta = {
        "features": FEATURES,
        "selected_regressor": reg_name,
        "selected_classifier": cls_name,
        "regression": regression,
        "classification": classification,
        "confusion_matrix": confusion_matrix(test.risk_level, classifier.predict(X_test), labels=[0, 1, 2]).tolist(),
        "feature_importance": dict(zip(FEATURES, map(float, importance))),
        "coefficients": dict(zip(FEATURES, map(float, coefficients))),
        "train_size": len(train),
        "test_size": len(test),
        "selection": "Five-fold cross-validation on the training partition",
    }
    MODEL_PATH.parent.mkdir(exist_ok=True)
    with NamedTemporaryFile(dir=MODEL_PATH.parent, delete=False) as tmp:
        temporary_path = Path(tmp.name)
    try:
        joblib.dump({"regressor": regressor, "classifier": classifier, "meta": meta}, temporary_path)
        os.replace(temporary_path, MODEL_PATH)
    finally:
        temporary_path.unlink(missing_ok=True)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
