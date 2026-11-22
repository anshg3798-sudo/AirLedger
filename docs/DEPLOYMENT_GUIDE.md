# Deployment

## Backend

Use a Docker-compatible service such as Render, set the root directory to backend and use its Dockerfile. The image uses Python 3.12, runs training at build time and serves Flask with Waitress. The container listens on the supplied PORT, with 8080 as the default. Configure `AIRLEDGER_CORS_ORIGINS` as the comma-separated exact frontend origins, including the HTTPS scheme. Verify `GET /api/health` over HTTPS before connecting the frontend.

For local container verification from the project root, use:

```sh
docker build -t airledger-backend backend
docker run --rm -p 5000:8080 airledger-backend
```

## Frontend

Select frontend as the Vercel project root. Use Node 22, the Vite preset, the `npm run build` build command and dist as the output directory. Set `VITE_API_URL` to the HTTPS backend origin before building. The Vercel rewrite allows deep links to the React pages. Use a separate project configuration or approved origins for previews.

Keep deployment credentials in hosting integrations or GitHub Secrets if deployment automation is later authorized. Confirm DNS, health, all four routes and a browser prediction before recording a live URL.
