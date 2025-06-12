import pytest
from fastapi.testclient import TestClient
from src.api.task_api import app

@pytest.fixture(scope="module")
def test_client():
    """Fixture to initialize the test client for the FastAPI app."""
    client = TestClient(app)
    return client

# Test case for successful task execution

def test_successful_task_execution(test_client):
    """Test case to validate successful task execution."""
    response = test_client.post("/execute_task", json={
        "task_name": "example_task",
        "parameters": {"param1": "value1"}
    })
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Task executed successfully."}

# Test case for unsuccessful task execution due to invalid input

def test_unsuccessful_task_execution(test_client):
    """Test case to validate unsuccessful task execution due to invalid input."""
    response = test_client.post("/execute_task", json={
        "task_name": "invalid_task",
        "parameters": {"param1": "invalid_value"}
    })
    assert response.status_code == 400
    assert response.json() == {"status": "error", "message": "Invalid task or parameters."}

# Test case for missing task_name in request

def test_missing_task_name(test_client):
    """Test case to validate error when task_name is missing in the request."""
    response = test_client.post("/execute_task", json={
        "parameters": {"param1": "value1"}
    })
    assert response.status_code == 400
    assert response.json() == {"status": "error", "message": "task_name is required."}

# Test case for missing parameters in request

def test_missing_parameters(test_client):
    """Test case to validate error when parameters are missing in the request."""
    response = test_client.post("/execute_task", json={
        "task_name": "example_task"
    })
    assert response.status_code == 400
    assert response.json() == {"status": "error", "message": "parameters are required."}