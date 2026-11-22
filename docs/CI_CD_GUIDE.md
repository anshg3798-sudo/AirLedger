# CI/CD and GitHub Actions

Continuous integration checks code whenever a configured event occurs. Continuous delivery makes a tested build ready for a deployment process. GitHub Actions executes YAML workflows on runners and exposes each step's output.

The two workflows trigger on pushes to main, pull requests targeting main and manual dispatch. Backend CI installs Python requirements, regenerates the artifact and runs unittest discovery. Frontend CI uses the npm lockfile, runs Vitest and produces a Vite build. Neither CI job needs a deployment token.

In the repository's Actions tab, select a workflow, then select a run and open its job. Expand the first failing step and reproduce its command locally with the same runtime version. After the workflow is on the default branch, use Run workflow to demonstrate manual dispatch. In a viva, open both jobs and explain why model training precedes API tests.

Deployment is initiated through configured hosting integrations or the host's deployment controls. The repository includes independent CI and deployment configuration. A deployment workflow is pending an approved target and credentials.
