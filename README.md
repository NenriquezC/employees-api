# 🧑‍💼 Employees API

A production-ready REST API for employee management built with FastAPI,
PostgreSQL and Docker. Features JWT authentication and full CRUD operations.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)

---

## 🚀 Overview

RESTful API that manages employee records with secure access control.
Built with a clean modular architecture, containerized with Docker Compose,
and ready to integrate with any frontend or mobile client.

---

## 🧰 Tech Stack

| Layer        | Technologies                              |
|--------------|-------------------------------------------|
| Backend      | Python 3.12, FastAPI, Uvicorn             |
| Auth         | JWT (python-jose), Passlib + Bcrypt       |
| Database     | PostgreSQL 15, SQLAlchemy ORM             |
| Validation   | Pydantic v2                               |
| DevOps       | Docker, Docker Compose                    |
| Testing      | Pytest, HTTPX                             |

---

## 🔐 Authentication Flow
POST /auth/register   → Create user account
POST /auth/login      → Returns JWT access token
Authorization: Bearer <token>  → Required for all employee endpoints

---

## 📋 API Endpoints

### Auth
POST /auth/register   → Register new user
POST /auth/login      → Login and get JWT token

### Employees (all require JWT)
GET    /employees/            → List all employees
POST   /employees/            → Create employee
GET    /employees/{id}        → Get employee by ID
PUT    /employees/{id}        → Update employee
DELETE /employees/{id}        → Delete employee

---

## ⚙️ Local Setup

### Prerequisites
- Docker and Docker Compose installed

### Run with Docker
```bash
git clone https://github.com/NenriquezC/employees-api.git
cd employees-api

# Create .env file
cp .env.example .env  # or create manually (see below)

# Start everything
docker-compose up --build
```

API: http://127.0.0.1:8000  
Swagger docs: http://127.0.0.1:8000/docs

### Environment variables (.env)
```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/employees_db
SECRET_KEY=your-secret-key-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📁 Project Structure
employees_api/
├── app/
│   ├── main.py        # FastAPI app entry point
│   ├── config.py      # Settings from .env
│   ├── database.py    # SQLAlchemy session
│   ├── models.py      # Database models
│   ├── schemas.py     # Pydantic schemas
│   ├── routes.py      # API endpoints
│   └── auth.py        # JWT + password hashing
├── tests/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

---

## 📌 Roadmap

- [ ] Pytest test suite
- [ ] CI/CD with GitHub Actions
- [ ] Role-based access control (admin / employee)
- [ ] Pagination and filtering

---

## 👤 Author

**Néstor Enríquez**  
Python Backend Developer | Data Engineering  
[GitHub](https://github.com/NenriquezC) · [LinkedIn](www.linkedin.com/in/nestor-enriquez-cifuentes-6447a650)
