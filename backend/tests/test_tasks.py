import pytest
from fastapi.testclient import TestClient
from ..app import app

client = TestClient(app)

# Mock task data
mock_task = {"title": "Test Task", "description": "This is a test task"}

updated_status = {"status": "completed"}

base_url = "api/v1"
task_id = 0


def test_create_task():
    response = client.post(f"{base_url}/tasks", json=mock_task)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["title"] == mock_task["title"]
    assert json_data["description"] == mock_task["description"]
    assert json_data["status"] == "pending"
    global task_id
    task_id = json_data["id"]


def test_get_tasks():
    response = client.get(f"{base_url}/tasks?page_no=1&page_size=10")
    assert response.status_code == 200
    json_data = response.json()
    assert "total" in json_data
    assert "records" in json_data
    assert isinstance(json_data["records"], list)


def test_update_task():
    global task_id
    response = client.put(f"{base_url}/tasks/{task_id}", json=updated_status)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "completed"


def test_delete_task():
    global task_id
    response = client.delete(f"{base_url}/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"
