# Sprint 5 — Model insights, verification and documentation

## Goal and user story

As a data scientist, I want to inspect model performance so that I can evaluate prediction quality.

## Tasks

Expose actual selections, show model comparisons and interpretation, add automated tests and wire CI.

## Acceptance criteria

Display holdout metrics, selected names, labelled confusion matrix, features and coefficients or tree importance. Run both automated suites.

## Implementation paths

backend/train.py, frontend/src/pages/ModelInsights.jsx, backend/tests/test_api.py, frontend/src/App.test.jsx, .github/workflows/, docs/

## Actual changes

Added standardized coefficients, metadata-based selection badges, API and UI suites, lockfile-based CI and deployment guides.

## Tests performed

Executed backend and frontend suites and a frontend production build. Remote CI and deployment await the project repository and hosting setup.

## Deliverables and status

Model Insights, automated checks and academic documentation. Implemented locally. See the testing report for execution status.

## Problems and improvements

The original linear model left the importance panel empty. Standardized coefficients explain the fitted regression. Windows blocked native Rollup, so the frontend uses Rollup's WebAssembly distribution.
