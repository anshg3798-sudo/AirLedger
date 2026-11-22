
# Definition of Done (DoD)

A feature or user story is considered complete when it satisfies the agreed quality standards.

## AirLedger Definition of Done Checklist

- [ ] The feature meets its specified acceptance criteria.
- [ ] The implementation works as expected.
- [ ] The feature integrates correctly with existing modules.
- [ ] Valid inputs produce the expected output.
- [ ] Invalid inputs and error conditions are handled properly.
- [ ] Relevant backend API or frontend tests pass.
- [ ] No known critical defects remain unresolved.
- [ ] Code is organized and readable.
- [ ] Relevant documentation is updated.
- [ ] The changes are reviewed before merging.

## Acceptance Criteria vs Definition of Done

| Acceptance Criteria | Definition of Done |
|---|---|
| Specific to an individual user story | Applies to all completed stories |
| Describes what a feature must achieve | Describes the quality standards required |
| Used to verify expected functionality | Used to verify overall completion |

## Application to AirLedger

For example, the AQI prediction feature must accept valid pollutant and weather inputs and return the predicted AQI and risk classification.

Its acceptance criteria describe these expected results. The Definition of Done additionally requires input validation, appropriate error handling, relevant tests and updated documentation.

The checklist is the team's proposed quality standard and should be confirmed during team review.
