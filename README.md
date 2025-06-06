# AI-Powered Attendance & HRMS Platform

This is a next-generation AI-powered Attendance & HRMS platform.

## Overview

This monorepo contains the backend microservices, frontend web application, mobile application, and infrastructure configurations for the platform.

**Key Features (Planned):**
*   AI-face recognition attendance
*   Multi-shift & contractor-centric features
*   Full HRMS suite (payroll, PMS, travel, onboarding/offboarding, LMS, ATS)
*   Predictive & smart AI enhancements
*   Flexible hosting options (self-hosted Docker or fully-managed AWS)
*   Robust reporting, analytics, compliance, and subscription/licensing engine
*   Mobile apps (React Native) and Web UI (React + TailwindCSS)

## Prerequisites

*   Docker & Docker Compose
*   Node.js (for frontend and mobile development, if contributing outside Docker)
*   Python 3.10+ (for backend development, if contributing outside Docker)
*   Access to a PostgreSQL database and Redis instance (if running services outside Docker Compose)

## Getting Started (Development)

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Set up environment variables:**
    *   Copy `.env.example` to `.env` at the root and fill in any master environment variables if needed.
    *   Each service in the `services/` directory has its own `.env.example` (e.g., `services/auth/.env.example`). For Docker Compose, these are typically referenced directly. For local development outside Docker, you might need to copy these to `.env` files within their respective service directories.

3.  **Build and run services using Docker Compose:**
    ```bash
    docker-compose -f docker-compose.dev.yml up --build
    ```
    This will build the images for all services defined in `docker-compose.dev.yml` and start them.

    *   Auth service will be available at `http://localhost:8001`
    *   Web client (Vite dev server) will be available at `http://localhost:5173`
    *   PostgreSQL (for auth) will be available on host port `54321`
    *   Redis will be available on host port `63791`

4.  **Install frontend dependencies (if not done by Docker or if developing locally):**
    For the web client (`web-client/`):
    ```bash
    cd web-client
    npm install # or yarn install / pnpm install
    # npm run dev # if not using docker-compose for the frontend
    cd ..
    ```
    For the mobile app (`mobile-app/`):
    ```bash
    cd mobile-app
    npm install # or yarn install
    # To run on an emulator/device:
    # npm run android
    # npm run ios
    cd ..
    ```

## Project Structure

Refer to `docs/ARCHITECTURE.md` for a detailed explanation of the project structure and microservice interactions.

## Environment Variables

Each service may require specific environment variables. Refer to the `.env.example` file in the root directory and within each service's directory (e.g., `services/auth/.env.example`) for a list of required variables.

Key global variables (if any, to be defined in root `.env`):
*   `COMPOSE_PROJECT_NAME`: Sets the project name for Docker Compose.
*   ... (any other global settings)

## Contributing

Please see `docs/CONTRIBUTING.md`.
