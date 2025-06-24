# 📝 Task Manager UI

A responsive, user-friendly React app for managing tasks, powered by Material UI and Axios, designed to work with a FastAPI backend.

---

## Tech Stack

- **React 19**
- **Material UI (MUI)**
- **Axios**
- **Node.js v22.11.0**

---

## Features

- View paginated task list
- Create, update (status), delete tasks
- Responsive and elegant Material UI layout
- Local time formatting
- Snackbar-based action toasts
- Confirmation before deletion

---

## Prerequisites

- Node.js `v22.11.0` and npm
- Backend running at `http://localhost:8000` or any other address. Accordingly update `public/config.js` file

---

## Local Development Setup

1. **Clone the Repository**

```bash
git clone https://github.com/pibytwo/task_manager.git
cd task_manager/frontend
```

2. **Install Dependencies**

```bash
npm install
```

3. **Configuration**

Update a `public/config.js` file with base url for backend:

```
REACT_APP_BASE_URL=http://localhost:8000/api/v1
```

4. **Start the React App**

```bash
npm start
```

---


## API Expectations

This app expects the following API endpoints from the backend:

| Method | Endpoint             | Description            |
|--------|----------------------|------------------------|
| POST   | `/tasks`             | Create a new task      |
| GET    | `/tasks`             | Get paginated tasks    |
| PUT    | `/tasks/{task_id}`   | Update task status     |
| DELETE | `/tasks/{task_id}`   | Delete a task          |

---

## To Do

- [ ] Add search/sort/filter functionality
- [ ] Task editing capability
- [ ] User authentication

---
