# Contributing Guidelines

Thank you for considering contributing to the HRMS Platform!

## Code Style

*   **Python:** PEP8 compliant. Use `black` for formatting and `isort` for import sorting. `flake8` or `pylint` for linting.
*   **JavaScript/TypeScript (React/React Native):** ESLint (Airbnb rules preferred, or project default), Prettier for formatting.
*   **Comments:** Write clear and concise comments. Use Google-style or NumPy-style docstrings for Python functions/classes.

## Commit Messages

Follow conventional commit message format:
`type(scope): short description`
E.g.:
*   `feat(attendance): add face detection module`
*   `fix(payroll): correct TDS calculation for X state`
*   `docs(setup): update docker compose instructions`
*   `refactor(auth): improve token generation logic`
*   `test(hrms): add unit tests for leave balance`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`.
Scope: module or area of the project (e.g., `auth`, `web-client`, `payroll`, `ci`).

## Branch Naming

*   `feature/<feature-name>` (e.g., `feature/payroll-generation`)
*   `bugfix/<bug-description>` (e.g., `bugfix/login-error-500`)
*   `hotfix/<fix-name>`
*   `chore/<task-name>`

## Pull Request (PR) Process

1.  Fork the repository.
2.  Create a new branch from `main` (or the relevant development branch).
3.  Make your changes, adhering to code style and adding tests where applicable.
4.  Ensure all tests pass.
5.  Commit your changes with meaningful messages.
6.  Push your branch to your fork.
7.  Create a PR to the `main` branch of the original repository.
8.  Provide a clear description of your changes in the PR. Link to any relevant issues.
9.  Code review will be conducted. Address any feedback.
10. Once approved, your PR will be merged.

## Setting up Pre-commit Hooks (Recommended)
Pre-commit hooks can help automatically format and lint your code before committing.
(Instructions to set up pre-commit with tools like `pre-commit` and configurations for `black`, `isort`, `flake8`, `eslint`, `prettier` will be added here once the tools are configured in the project.)

Example placeholder for pre-commit setup:
```bash
# pip install pre-commit  (if not already installed)
# pre-commit install
```
A `.pre-commit-config.yaml` will be added to the root of the project.

## Code Review Guidelines
*   Be respectful and constructive.
*   Focus on the code and the problem it solves.
*   Explain your reasoning for requested changes.
