# Testing

From backend, train using `python train.py`, then run `python -m unittest discover -s tests -v`. The tests exercise Flask's request interface, invalid JSON and ranges, budgets and tiers, dashboard totals, forecast dates, probability labels and train-only scaling.

From frontend, run `npm ci`, `npm test` and `npm run build`. Vitest uses jsdom and a mocked API. Chart containers are stubbed in these tests because jsdom has no chart layout engine. Use a browser against the running stack to check chart rendering and frontend/backend integration.

For the manual lab protocol, see [Project demo](PROJECT_DEMO.md). Current outcomes are recorded in the [testing report](../agile/TESTING_REPORT.md).
