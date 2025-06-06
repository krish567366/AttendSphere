# Setup Guide

This guide provides detailed instructions for setting up the development environment and deploying the application.

## Local Development Setup

### Prerequisites
*   Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
*   Docker & Docker Compose: [Install Docker](https://docs.docker.com/get-docker/) (Docker Desktop includes Compose)
*   Node.js (latest LTS, e.g., v18 or v20): [Install Node.js](https://nodejs.org/) (needed for `npm`/`yarn` if working on frontend/mobile outside Docker, or for some pre-commit hooks)
*   Python (3.10+): [Install Python](https://www.python.org/downloads/) (if developing backend services outside Docker)

### 1. Clone Repository
```bash
git clone <your-repository-url>
cd <repository-directory>
```

### 2. Environment Variables
This project uses `.env` files for managing environment variables. Example files (`.env.example`) are provided at the root and within each service directory.

*   **Root `.env` (Optional):**
    You can create a `.env` file in the project root for Docker Compose specific variables like `COMPOSE_PROJECT_NAME`.
    ```bash
    cp .env.example .env # If .env.example exists at root and is needed
    ```
*   **Service-Specific `.env` files:**
    The `docker-compose.dev.yml` is configured to use the `.env.example` files directly from each service folder (e.g., `services/auth/.env.example`).
    For local development *without* Docker, you would typically copy the `.env.example` to `.env` within that service's directory and modify it.
    Example for `auth-service`:
    ```bash
    # cd services/auth
    # cp .env.example .env # (and customize if not using docker-compose defaults)
    # cd ../..
    ```
    **Important:** Ensure database URLs, secrets, and API keys are correctly set. For development with the provided Docker Compose, the default URLs in `.env.example` files (e.g., for `auth-service` connecting to `postgres_auth:5432`) are usually sufficient.

### 3. Running with Docker Compose (Recommended)
This is the easiest way to get all services running.
```bash
docker-compose -f docker-compose.dev.yml up --build -d
```
*   `--build`: Forces Docker to build the images before starting containers.
*   `-d`: Runs containers in detached mode.

To view logs:
```bash
docker-compose -f docker-compose.dev.yml logs -f
# Or for a specific service:
# docker-compose -f docker-compose.dev.yml logs -f auth-service
```

To stop services:
```bash
docker-compose -f docker-compose.dev.yml down
```

### 4. Frontend Development (Web Client)
The web client is located in `web-client/`.
If using Docker Compose, it should be running on `http://localhost:5173` (Vite default).

To run locally (outside Docker, after `npm install` in `web-client/`):
```bash
cd web-client
npm run dev
cd ..
```

### 5. Mobile App Development
The mobile app is in `mobile-app/`.
Development typically involves running on an emulator or physical device.

To run locally (after `npm install` in `mobile-app/`):
```bash
cd mobile-app
npm run android  # Or `npm run ios`
cd ..
```
Ensure you have the necessary Android SDK / iOS Xcode setup.

### 6. Backend Service Development (Outside Docker)
If you need to run a backend service outside of Docker (e.g., for debugging with a local IDE):
1.  Ensure PostgreSQL and Redis are accessible (either from Docker Compose or running locally).
2.  Navigate to the service directory (e.g., `cd services/auth`).
3.  Create a virtual environment and install dependencies from `requirements.txt`.
    ```bash
    python -m venv venv
    source venv/bin/activate # or venv\Scriptsctivate for Windows
    pip install -r requirements.txt
    ```
4.  Set up the `.env` file with correct database URLs etc.
5.  Run the FastAPI app using Uvicorn:
    ```bash
    uvicorn app.main:app --reload --port 8001
    ```

## Secrets Management (Production)
**DO NOT COMMIT ACTUAL SECRETS TO THE REPOSITORY.**
For production, use a proper secrets management solution:
*   AWS Secrets Manager
*   HashiCorp Vault
*   Environment variables injected by the CI/CD system or container orchestrator.

## Deployment to AWS (Placeholder)
(Detailed steps for AWS deployment using ECS/EKS, Terraform/CloudFormation will be added here.)

1.  **Build production Docker images.**
2.  **Push images to a container registry (e.g., AWS ECR).**
3.  **Provision infrastructure using Terraform/CloudFormation (see `infra/aws/`).**
    *   VPC, Subnets, Security Groups
    *   ECS Cluster or EKS Cluster
    *   RDS for PostgreSQL
    *   ElastiCache for Redis
    *   S3 for static assets / file storage
    *   IAM Roles
4.  **Deploy services to ECS/EKS.**
5.  **Configure Load Balancers and DNS.**
