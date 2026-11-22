# Local setup

Use Python 3.12 and Node.js 22.12 or newer. Follow the [Windows setup](../README.md#run-locally) or run these commands from the project root on macOS or Linux:

```sh
python3.12 -m venv .venv
cd backend
../.venv/bin/python -m pip install -r requirements.txt
../.venv/bin/python train.py
../.venv/bin/python app.py
```

In a second terminal, run `cd frontend`, `npm ci` and `npm run dev`. Open http://localhost:5173. If Flask uses a different port, set `AIRLEDGER_DEV_API_URL` before starting Vite. Alternatively, set `VITE_API_URL` in frontend/.env.local and include the frontend origin in `AIRLEDGER_CORS_ORIGINS` on the backend. Restart Flask after retraining.

To check Flask directly, run `curl http://127.0.0.1:5000/api/health`. A 503 response instructs you to train the artifact first.
