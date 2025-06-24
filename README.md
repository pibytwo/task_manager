
# Task Manager App – Dockerized

This is a full-stack **Task Manager** app with a React frontend and FastAPI backend, both containerized using Docker Compose.

Refer to respective Readme files of each service (backend, frontend) for more details and dev setup

---

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Local Setup

1. **Clone the repo**
   ```bash
    git clone https://github.com/pibytwo/task_manager.git
    cd task_manager
   ```

2. **Run the app using Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the app**
   - **Frontend (UI)**: [http://localhost](http://localhost)
   - **Backend (API)**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Environment Details

### Backend (FastAPI)
- Exposed on port **8000**
- Uses environment variables:
  - `ENV=uat` → skips `.env` loading
  - `DB_NAME=tasks` → for SQLite file
- SQLite data stored in `/app/data` (mounted volume)

### Frontend (React + NGINX)
- Built via multi-stage Dockerfile
- Served using **NGINX** on port **80**
- Assumes `public/config.js` is injected with API URL at runtime using `REACT_APP_BASE_URL`

---


