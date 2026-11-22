# Acceptance criteria

- **AL-1** Preserve 1,095 rows and 13 ordered features. Keep scaling and selection independent of the 219-record holdout. Record both historic and current scores.
- **AL-2** A complete valid payload returns finite AQI and labelled probabilities. Invalid JSON, missing inputs and invalid types receive appropriate errors.
- **AL-3** AQI 100 yields zero overshoot. Positive overshoot and recommendation tiers agree with the displayed AQI. Decimal values receive the expected band.
- **AL-4** Return 60 observation dates, seven location aggregates, twelve months and seven successive simulated Delhi dates.
- **AL-5** Display holdout metrics, selected names, labelled confusion matrix, features and coefficients or tree importance. Run both automated suites.
