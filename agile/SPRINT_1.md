# Sprint 1 — Dataset and machine learning

## Goal and user story

As an analyst, I want a clean dataset and baseline models so that AQI can be predicted reliably.

## Tasks

Inspect the supplied data, reproduce the historical run, compare all five candidates, train and serialize the winners.

## Acceptance criteria

Preserve 1,095 rows and 13 ordered features. Keep scaling and selection independent of the 219-record holdout. Record both historic and current scores.

## Implementation paths

backend/train.py, backend/schema.py, backend/data/delhi_aqi_data.csv

## Actual changes

Reproduced the original headline metrics. Added training-only pipeline fitting, cross-validation selection and atomic model artifact writes.

## Tests performed

Executed original and corrected training, then verified scaler means and evaluation metadata through the backend tests.

## Deliverables and status

Serialized model bundle and reproducible training command. Implemented locally. See the testing report for execution status.

## Problems and improvements

The original scaler saw all rows and the holdout selected the winner. Fixed both issues. The selected classifier changed to Logistic Regression.
