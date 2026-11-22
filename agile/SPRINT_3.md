# Sprint 3 — Budget and recommendations

## Goal and user story

As an official, I want to see pollution-budget overshoot and recommended actions so that I can respond proportionately.

## Tasks

Implement the inclusive AQI 100 budget, preserve the gauge and budget bar, and check recommendation thresholds.

## Acceptance criteria

AQI 100 yields zero overshoot. Positive overshoot and recommendation tiers agree with the displayed AQI. Decimal values receive the expected band.

## Implementation paths

backend/app.py, frontend/src/utils/aqi.js, frontend/src/pages/Predict.jsx

## Actual changes

Aligned budget, decimal band classification and recommendation thresholds around one displayed prediction. Kept the original gauge and risk badge.

## Tests performed

Executed category boundary and budget tier tests, plus the prediction display test.

## Deliverables and status

Gauge, overshoot calculation and four graded tiers. Implemented locally. See the testing report for execution status.

## Problems and improvements

Original integer intervals left decimal gaps. Inclusive upper bounds cover the gaps.
