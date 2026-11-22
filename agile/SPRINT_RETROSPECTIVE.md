
## Continuous Improvement Analysis

The implementation highlighted several areas where the development process and product can be improved.

### What Went Well

- Model training became more reliable after introducing training pipelines.
- API boundary tests helped identify AQI threshold-related issues.
- The frontend build was made compatible with the development environment.
- The project includes separate backend and frontend automated test suites.

### Challenges Observed

- Training-time preprocessing and model selection needed stricter separation.
- Decimal AQI values exposed gaps in threshold handling.
- Windows environment compatibility affected the native Rollup dependency.
- Frontend and backend integration requires consistent API response formats.

### Proposed Improvement Actions

| Improvement | Expected Benefit |
|---|---|
| Expand automated unit and API tests | Better defect detection |
| Define API contracts before integration | Reduce integration issues |
| Improve feature-importance reporting | Better model interpretability |
| Integrate live CPCB and weather data | More relevant environmental information |
| Evaluate proper time-series forecasting | More realistic future predictions |

These are proposed improvements, not completed activities.

## Future Retrospective Action Log

| Action Item | Responsible Member | Status |
|---|---|---|
| Expand automated test coverage | To be assigned | Proposed |
| Document API response formats | To be assigned | Proposed |
| Review model interpretability | To be assigned | Proposed |
| Evaluate forecasting alternatives | To be assigned | Proposed |

The team should update this section after conducting an actual retrospective meeting.
