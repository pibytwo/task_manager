# 📝 Task Manager Backend

A simple task management REST API built using **FastAPI** and **SQLAlchemy**. This API allows users to **create**, **view (paginated)**, **update**, and **delete** tasks with status tracking.

---

## Features

- Create new tasks  
- Fetch paginated list of tasks  
- Update task status (`pending` / `completed`)  
- Delete tasks  
- Modular project structure (routers, models, CRUD ops, logger)  

---


## Local Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pibytwo/task_manager.git
cd task_manager/backend
```

### 2. Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install python-dotenv
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```ini
ENV=dev
DB_NAME=tasks
```

> Uses SQLite by default. Ensure `DB_NAME` is set.

### 5. Run the App

```bash
python app.py
```

Or with `uvicorn`:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

---


## Run Test Cases

```bash
pip install pytest httpx
pytest ./tests/
```

---

## API Endpoints

| Method | Endpoint       | Description           | Request Body / Params     |
|--------|----------------|-----------------------|----------------------------|
| POST   | `/tasks`       | Create a new task     | `title`, `description`     |
| GET    | `/tasks`       | Fetch paginated tasks | `page_no`, `limit`         |
| PUT    | `/tasks/{id}`  | Update task status    | `status`                   |
| DELETE | `/tasks/{id}`  | Delete a task         | –                          |

---

## To-Do / Improvements

- [ ] Add authentication layer  
- [ ] Add DB migrations (e.g., Alembic)  
- [ ] Add integration tests   

---