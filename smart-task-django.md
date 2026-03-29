# Production-Ready Smart Task Management API with Django & JWT

## Overview
A backend API built with Django and Django REST Framework (DRF) to manage tasks with a smart auto-priority logic system and JWT-based authentication.

## Project Type
BACKEND

## Success Criteria
- [ ] Users can register and login, receiving JWT tokens.
- [ ] Authenticated users can perform full CRUD operations on their tasks.
- [ ] Smart Priority Logic automatically assigns priority (HIGH $<1$ day, MEDIUM $<3$ days, LOW otherwise) when creating/updating tasks.
- [ ] All API endpoints return clean, properly formatted JSON responses with adequate error handling.

## Tech Stack
- **Framework:** Django (Core structure & ORM)
- **API Layer:** Django REST Framework (RESTful routing & serialization)
- **Authentication:** djangorestframework-simplejwt (JWT Auth)
- **Database:** SQLite (default Django DB, easily swappable to PostgreSQL)

## File Structure
```text
smart-task-api/
├── manage.py
├── requirements.txt
├── README.md
├── core/                # Project settings & routing
├── users/               # Authentication app (Register, Login, JWT)
├── tasks/               # Task management app (CRUD APIs)
└── services/            # Business logic (Priority auto-calculation)
```

## Task Breakdown

### TASK-1: Project Setup & Apps Initialization
- **Agent:** `@backend-specialist`
- **Skills:** `app-builder`, `clean-code`
- **Priority:** P1
- **Dependencies:** None
- **INPUT:** Run `django-admin startproject core .` and `python manage.py startapp users` and `python manage.py startapp tasks`.
- **OUTPUT:** Django project initialized with `core`, `users`, and `tasks` apps linked in `settings.py`.
- **VERIFY:** `python manage.py check` runs without errors.

### TASK-2: Task Models & Database Migrations
- **Agent:** `@database-architect` / `@backend-specialist`
- **Skills:** `database-design`
- **Priority:** P1
- **Dependencies:** TASK-1
- **INPUT:** Create `Task` model in `tasks/models.py` (fields: title, description, deadline, priority, status, user [ForeignKey]).
- **OUTPUT:** Models created and migrated (`python manage.py makemigrations` & `migrate`).
- **VERIFY:** `Task` table exists in SQLite database schema.

### TASK-3: JWT Authentication System
- **Agent:** `@security-auditor` / `@backend-specialist`
- **Skills:** `api-patterns`
- **Priority:** P1
- **Dependencies:** TASK-1, TASK-2
- **INPUT:** Install `djangorestframework-simplejwt`, configure in `settings.py`, create User Serializers and registration/login views.
- **OUTPUT:** Endpoints `POST /api/register/` and `POST /api/login/` working.
- **VERIFY:** Successfully register a user and obtain a JWT access token upon login.

### TASK-4: Smart Priority Logic Service
- **Agent:** `@backend-specialist`
- **Skills:** `clean-code`, `python-patterns`
- **Priority:** P1
- **Dependencies:** TASK-2
- **INPUT:** Create `services/priority_calculator.py` to auto-calculate priority based on deadline vs. current time.
- **OUTPUT:** Isolated service function returning HIGH, MEDIUM, or LOW based on deadline.
- **VERIFY:** Unit tests for `priority_calculator` evaluating <1 day, <3 days, and >3 days correctly.

### TASK-5: Tasks API endpoints
- **Agent:** `@backend-specialist`
- **Skills:** `api-patterns`
- **Priority:** P1
- **Dependencies:** TASK-3, TASK-4
- **INPUT:** Create serializers and views (or ViewSets) for Tasks CRUD, integrating the Smart Priority Logic service dynamically during task creation/updates.
- **OUTPUT:** Endpoints `GET /api/tasks/`, `POST /api/tasks/`, `PUT /api/tasks/<id>/`, `DELETE /api/tasks/<id>/` operational and protected.
- **VERIFY:** Authenticated API requests successfully manage tasks, and priority fields are correctly assigned behind the scenes.

### TASK-6: Final Polish & Documentation
- **Agent:** `@frontend-specialist` (or `@backend-specialist`)
- **Skills:** `documentation-templates`
- **Priority:** P2
- **Dependencies:** ALL previous tasks
- **INPUT:** Implement task filtering in `GET /api/tasks/`, finalize README.md with setup instructions and API docs.
- **OUTPUT:** Polished API endpoints and complete `README.md`.
- **VERIFY:** README renders correctly and provides all necessary information for a developer to run the project.

## ✅ PHASE X: Verification Checklist
- [ ] Run Lint / Type check (if applicable, e.g., flake8/mypy)
- [ ] Security Scan (no leaked `.env` keys, JWT securely configured)
- [ ] Unit/Integration tests pass for priority calculation and API endpoints
- [ ] Manual test: End-to-end task creation flow with Postman/cURL
