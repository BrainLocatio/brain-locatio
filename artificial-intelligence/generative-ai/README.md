# 📌 Project Overview

This project provides technical articles retrieved through semantic search using LLaMA, with content generation powered by the OpenAI API.

## System-level Architecture

Frontend: Node.js, React, HTML, Tailwind CSS

Backend-for-Frontend (BFF)
- Separation of concerns
  - The semantic search service should focus on search logic, not auth, rate limiting, request shaping, etc.
  - The backend layer can handle authentication, validation, caching, request formatting, and aggregation. 
  Enforce authorization, manage API keys, and hide service internals.

Semantic search service

## Backend-for-Frontend (BFF) Service

- Code-level Architecture: Layered architecture

API design

|                         |          |
|-------------------------|----------|
| **API**                 | REST     |
| **Framework**           | FastAPI  |
| **Data validation**     | Pydantic |  

## Infrastructure and Deployment Architecture

|                   |                      |
|-------------------|----------------------|
| **Deployment / Runtime:**    | Docker, Kubernetes   |
| **Infrastructure** | Terraform            |

# 🏛️ System architecture pillars

## Reliable architecture

TBD

# 🛠 Development

|                       |                                                            |
|-----------------------|------------------------------------------------------------|
| **IDE & Environment** | PyCharm with Python virtual environment                    |
| **Testing**           | Pytest framework                                           |
| **Local Kubernetes**  | Minikube (lightweight local cluster) managed via Terraform |  
| **CI/CD**             | GitHub Actions workflow simulation for local testing       |  
