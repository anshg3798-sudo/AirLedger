# Sprint 1 — Dataset and machine learning

## Goal and user story

As an analyst, I want a clean dataset and baseline models so that AQI can be predicted reliably.

## Tasks

removed

## Actual changes

Reproduced the original headline metrics. Added training-only pipeline fitting, cross-validation selection and atomic model artifact writes.

## Tests performed

Executed original and corrected training, then verified scaler means and evaluation metadata through the backend tests.

## Deliverables and status

Serialized model bundle and reproducible training command. Implemented locally. See the testing report for execution status.

## Problems and improvements

The original scaler saw all rows and the holdout selected the winner. Fixed both issues. The selected classifier changed to Logistic Regression.
