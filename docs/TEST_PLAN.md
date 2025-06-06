# Test Plan

This document outlines the testing strategy for the HRMS Platform.

## Testing Goals
*   Ensure correctness and reliability of all features.
*   Achieve high code coverage.
*   Prevent regressions.
*   Validate performance and scalability (future).

## Testing Levels

### 1. Unit Tests
*   **Purpose:** Test individual functions, methods, and components in isolation.
*   **Tools:**
    *   Python (Backend Services): `pytest`, `unittest` (pytest preferred). Mocks using `unittest.mock` or `pytest-mock`.
    *   React (Web Client): Jest, React Testing Library.
    *   React Native (Mobile App): Jest, React Native Testing Library.
*   **Location:** Within each service/app's `tests/` directory (e.g., `services/auth/tests/`).
*   **Coverage Target:** Aim for ≥ 80% for backend services, ≥ 70% for frontend components.
*   **Execution:** Run automatically in CI pipeline on every push/PR.

### 2. Integration Tests
*   **Purpose:** Test interactions between components or services. E.g., API endpoint testing, service-to-database interaction.
*   **Tools:**
    *   Python (Backend Services): `pytest` with `httpx` (for FastAPI) or test clients. Test databases.
    *   Frontend: React Testing Library interacting with mocked API backends (MSW - Mock Service Worker).
*   **Location:** Within `tests/` directories, often in subfolders like `tests/integration/`.
*   **Execution:** Run automatically in CI pipeline.

### 3. End-to-End (E2E) Tests
*   **Purpose:** Test complete user flows through the application.
*   **Tools:**
    *   Web Client: Playwright or Cypress.
    *   Mobile App: Detox or Appium.
*   **Scenarios (Examples):**
    *   User registration → Login → Face Punch → View Dashboard.
    *   Apply for Leave → Manager Approval → Check Leave Balance.
    *   Contractor Onboarding → Shift Assignment → Attendance Record.
    *   Generate Payroll → Verify Payslip.
*   **Execution:** Run in CI pipeline, possibly less frequently than unit/integration tests (e.g., nightly or on release branches).

## Test Data & Mocking
*   **Fixtures:** Use `pytest` fixtures for setting up test data for backend tests.
*   **Mocking:**
    *   `unittest.mock` / `pytest-mock` for Python.
    *   Jest mocks for frontend.
    *   MSW (Mock Service Worker) for mocking API requests in frontend tests.
*   **Test Databases:** Use separate, temporary databases for integration tests. Alembic can be used to manage schema for test DBs.

## How to Execute Tests

### Backend (Python - e.g., Auth service)
```bash
cd services/auth
# (Activate virtual environment if not using Docker)
pytest
# For coverage:
# pytest --cov=app --cov-report=html
```
(Requires `pytest.ini` and `coverage.ini` to be configured).

### Frontend (Web Client - React)
```bash
cd web-client
npm test
# For coverage:
# npm test -- --coverage
```

### Mobile App (React Native)
```bash
cd mobile-app
npm test
```

## Coverage Reporting
Coverage reports will be generated and can be uploaded to services like Codecov or SonarQube.

## Future Testing Types
*   Performance/Load Testing (e.g., k6, Locust, JMeter).
*   Security Testing (SAST, DAST).
*   Usability Testing.
