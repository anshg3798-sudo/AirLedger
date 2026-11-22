# Delivery inventory and release status

```text
AirLedger/
├── .github/workflows/        Backend and frontend CI
├── agile/                    Backlog, five sprints, criteria and testing evidence
├── backend/
│   ├── data/                 Original Delhi-NCR CSV
│   ├── tests/                Flask integration and model checks
│   ├── app.py, schema.py and train.py
│   └── requirements.txt and Dockerfile
├── docs/                     Audit, release inventory and technical guides
├── frontend/
│   ├── src/
│   │   ├── components/      Shared cards, navigation, gauge and loading states
│   │   ├── hooks/           Fetch lifecycle
│   │   ├── pages/           Dashboard, prediction, simulation and model insights
│   │   ├── services/        REST client
│   │   └── utils/           AQI bands and risk styling
│   ├── package.json and package-lock.json
│   └── Vite, Tailwind, PostCSS and Vercel configuration
├── .gitignore
└── README.md
```

## Modified from the supplied archive

- `README.md`
- `backend/app.py`, `backend/train.py`, `backend/requirements.txt`
- `frontend/package.json`, `frontend/vite.config.js`
- `frontend/src/App.jsx`, `frontend/src/components/Sidebar.jsx`
- `frontend/src/pages/Dashboard.jsx`, `Predict.jsx`, `Forecast.jsx`, `ModelInsights.jsx`
- `frontend/src/services/api.js`, `frontend/src/utils/aqi.js`

The original CSV SHA-256 is `F5B5073215CD75B53E6408AA7FF34096826166BB58E9A8162032D54B4A1060C4`, and matches the delivered CSV.

## Added

- `.gitignore`
- `.github/workflows/backend-ci.yml` and `frontend-ci.yml`
- `backend/schema.py`, `backend/tests/test_api.py`, `backend/Dockerfile`, `backend/.dockerignore`
- `frontend/package-lock.json`, `frontend/src/App.test.jsx`, `frontend/.env.example`, `frontend/vercel.json`
- `docs/PROJECT_AUDIT.md`, `ARCHITECTURE.md`, `API_DOCUMENTATION.md`, `SETUP_GUIDE.md`, `TESTING_GUIDE.md`, `CI_CD_GUIDE.md`, `DEPLOYMENT_GUIDE.md`, `PROJECT_DEMO.md`, `VIVA_PREPARATION.md`, `DELIVERY.md`
- `agile/PRODUCT_BACKLOG.md`, `USER_STORIES.md`, `ACCEPTANCE_CRITERIA.md`, `DEFINITION_OF_DONE.md`, `SPRINT_1.md` through `SPRINT_5.md`, `SPRINT_REVIEW.md`, `SPRINT_RETROSPECTIVE.md`, `TESTING_REPORT.md`

## GitHub and hosting

The archive had no Git directory or remote. Local Git author settings were present, but GitHub account identity and intended repository were not confirmed. There are no commit hashes, issues, pull requests, remote CI runs or live deployment URL for this delivery. The two workflows are ready to run after repository setup. The Dockerfile and Vercel routing are included for hosting configuration. Docker image build and deployment were not executed here.

If the confirmed destination already has Git history, create a feature branch from its existing default branch and integrate the delivered changes. For a new, empty destination, run the following from the extracted project after confirming the target. Replace the example values with the verified author details and exact repository URL:

```sh
git init -b main
git config --local user.name "Verified GitHub author name"
git config --local user.email "Verified GitHub author email"
git remote add origin "https://github.com/OWNER/REPOSITORY.git"
git status --short
git add .
git commit -m "feat: complete AirLedger Agile lab project"
git log -1 --oneline
git push -u origin main
```

After the first push, verify the commit on GitHub and inspect the backend and frontend Actions runs. Use the separate deployment guide when a hosting target is confirmed.
