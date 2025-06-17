# 📌 Project Overview

This project provides technical articles retrieved through semantic search using LLaMA, with content generation powered 
by the OpenAI API. 

Additionally, it integrates a third-party WeatherAPI to provide weather data, which is used to generate non-technical 
articles related to current weather conditions.

## System-level Architecture

Frontend: Node.js, React, HTML, Tailwind CSS

Backend-for-Frontend (BFF)
- auth, rate limiting, request shaping (formatting)
  - Request shaping means modifying or enhancing incoming requests before they reach the actual business logic (like search, inference, or other core functionality).
- validation, caching, and aggregation
  - Aggregation means combining data from multiple sources or services into a single, unified response. E.g. semantic + weather
- Enforce authorization, manage API keys, and hide service internals.

Semantic search service
- perform calls to OpenAI if needed, and do the semantic search in text

## Backend-for-Frontend (BFF) Service

- Code-level Architecture: Layered architecture
- Handler pattern (gRPC)

API design

|                         |          |
|-------------------------|----------|
| **API**                 | REST     |
| **Framework**           | FastAPI  |
| **Data validation**     | Pydantic |

DB design
PostgreSQL, database for web application, docker compose
pydantic settings

## Semantic search microservice
- Code-level Architecture: Layered architecture

API design

|                         |          |
|-------------------------|----------|
| **API**                 | gRPC     |
| **Framework**           | FastAPI  |
| **Data validation**     | Protobuf |

## Infrastructure and Deployment Architecture

|                   |                     |
|-------------------|---------------------|
| **Deployment / Runtime:**    | Docker, Kubernetes  |
| **Infrastructure** | Terraform           |

- Frontend talks to BFF using internal DNS, e.g. http://bff-svc.default.svc.cluster.local.
- Backend (BFF) is deployed as a ClusterIP service meaning it’s internal only.

# 🏛️ System architecture pillars

## Reliable architecture

TBD

# 🛠 Development

|                       |                                                            |
|-----------------------|------------------------------------------------------------|
| **IDE & Environment** | PyCharm with Python virtual environment                    |
| **Testing**           | Pytest, Unittest frameworks                                |
| **Local Kubernetes**  | Minikube (lightweight local cluster) managed via Terraform |  
| **CI/CD**             | GitHub Actions workflow simulation for local testing       |  
