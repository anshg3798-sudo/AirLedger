
## Agile Testing Approach

Testing is integrated throughout the AirLedger development process instead of being postponed until the end.

| Sprint | Testing activity |
|---|---|
| Sprint 1 | Evaluate regression and classification models |
| Sprint 2 | Verify AQI prediction and invalid input handling |
| Sprint 3 | Check pollution-budget calculations and recommendation tiers |
| Sprint 4 | Verify dashboard data and forecast API responses |
| Sprint 5 | Review model insights, automated tests and documentation |

## Current Test Evidence

- Backend automated test suite: 9 tests passed.
- Frontend automated test suite: 6 tests passed.
- API validation includes missing fields, invalid numeric values and incorrect JSON requests.
- AQI category boundaries and pollution-budget calculations are tested.
- Frontend tests cover dashboard, prediction, forecast and model insights.
- A production frontend build was completed successfully.

## Known Limitations

- An automated unit-test suite for individual model-training components can be expanded.
- Feature-importance reporting depends on the attributes exposed by the selected model.
- The frontend production build reports a JavaScript chunk larger than 500 kB.

Future testing can include broader unit-test coverage, additional API edge cases and automated end-to-end browser tests.
