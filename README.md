# CI-CD-Pipeline-for-Deepfake-Processing

## Overview
This project demonstrates a **production-ready CI/CD pipeline** for deploying a **deepfake detection API**.  
The focus of this work is **DevOps automation, reliability, and deployment**, not machine-learning research.

A mock deepfake detection service is used to represent inference behavior, allowing the pipeline to be fully automated and production-validated.

---

## Key Objectives
- Automate testing, linting, and quality checks
- Build and version Docker images
- Publish container images to a registry
- Deploy automatically to AWS EC2
- Validate deployments using health checks
- Demonstrate server-side processing via an API endpoint

---

## Architecture
Developer
   |
GitHub Repository
   |
GitHub Actions (CI/CD)
   |
Docker Image (Docker Hub)
   |
AWS EC2 (Docker Runtime)
   | 
Deepfake Detection API (FastAPI)

---

## CI/CD Pipeline

### Continuous Integration (CI)
Triggered on every push and pull request.

CI stages:
- Code checkout
- Dependency installation
- Code formatting validation (Black)
- Linting (Flake8)
- Unit tests (Pytest)
- Coverage reporting
- Docker image build
- Smoke test using `/health` endpoint

CI ensures that only **validated, high-quality code** progresses to deployment.

---

### Continuous Deployment (CD)
Triggered automatically on merge to the `main` branch.

CD stages:
- Build versioned Docker image (commit SHA)
- Push image to Docker Hub
- Deploy container to AWS EC2
- Stop previous container (if running)
- Start new container
- Post-deployment health validation

Deployments are **fully automated** and **idempotent**.

---

## API Endpoints

### Health Check
Used by CI/CD to verify application readiness.

GET /health

Response:
```json
{ "status": "ok" }

--Deepfake Detection (Mock Inference)

Demonstrates server-side processing.

POST /detect

Request:

{
  "audio_url": "sample.wav"
}


Response:

{
  "score": 0.87,
  "verdict": "fake"
}


Note:
The detection logic is intentionally lightweight. The purpose is to demonstrate deployment, automation, and operational readiness, not ML model accuracy.

--> Server-Side Processing Confirmation

Detection logic runs inside a Docker container

Container runs on AWS EC2

Results are computed on the server

Client only sends input and receives output

Stopping the container stops the API, confirming true server-side execution.

***Deployment Environment

Cloud Provider: AWS

Compute: EC2 (Docker runtime)

Registry: Docker Hub

CI/CD: GitHub Actions

****Security & Best Practices

Non-root Docker container

Environment-based configuration

Immutable image versioning (commit SHA)

Automated rollback via image redeploy

Health-based deployment validation
