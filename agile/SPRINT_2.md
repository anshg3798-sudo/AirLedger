# Sprint 2 — AQI prediction

## Goal and user story

As a user, I want to enter environmental conditions and receive predicted AQI and a risk classification instantly.

## Tasks

Validate request types and bounds, derive calendar values, wire form validation and presets, and return useful errors.

## Acceptance criteria

A complete valid payload returns finite AQI and labelled probabilities. Invalid JSON, missing inputs and invalid types receive appropriate errors.

## Implementation paths

backend/app.py, backend/schema.py, frontend/src/pages/Predict.jsx, frontend/src/services/api.js

## Actual changes

Added bounded numeric validation, consistent HTTP errors and a relative development API route. Blank form values remain blank for validation.

## Tests performed

Executed prediction, malformed JSON and CORS API tests. Vitest verified validation, seasonal preset submission and rendered results.

## Deliverables and status

Prediction API and seasonal input form. Implemented locally. See the testing report for execution status.

## Problems and improvements

The original API silently assigned zero to missing inputs. It now rejects missing inputs and derives is_weekend.
