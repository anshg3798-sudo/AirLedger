# Sprint 4 — Dashboard and simulation

## Goal and user story

As a planner, I want pollution trends and a short-term outlook so that I can understand environmental patterns.

## Tasks

Aggregate by date, month, location and risk class. Add budget counts. Bound and label the forecast simulation.

## Acceptance criteria

Return 60 observation dates, seven location aggregates, twelve months and seven successive simulated Delhi dates.

## Implementation paths

backend/app.py, frontend/src/pages/Dashboard.jsx, frontend/src/pages/Forecast.jsx, frontend/src/components/Sidebar.jsx

## Actual changes

Added budget counts and a trend threshold, validated forecast inputs, used Delhi calendar dates and adapted navigation to narrow viewports.

## Tests performed

Executed dashboard and forecast API contract tests and page tests for loading, retry and simulation display.

## Deliverables and status

Dashboard and seven-day scenario outlook. Implemented locally. See the testing report for execution status.

## Problems and improvements

Original month UI control was ignored. Legacy API month overrides are honored, while the form uses the dates' actual month.
