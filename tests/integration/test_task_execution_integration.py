import pytest
from sources.task_execution import execute_task  # Assuming execute_task is the main function to be tested


def test_execute_task_success():
    """Test successful task execution."""
    task_input = {'steps': ['Step 1', 'Step 2'], 'parameters': {}}
    result = execute_task(task_input)
    assert result['status'] == 'success'
    assert 'output' in result


def test_execute_task_failure():
    """Test task execution with invalid input."""
    task_input = {'steps': [], 'parameters': {}}  # Invalid input
    result = execute_task(task_input)
    assert result['status'] == 'failure'
    assert 'error' in result


def test_execute_task_partial_success():
    """Test task execution with some steps failing."""
    task_input = {'steps': ['Step 1', 'Step 2', 'Step 3'], 'parameters': {}}
    result = execute_task(task_input)
    assert result['status'] in ['partial_success', 'success']
    assert 'output' in result or 'partial_output' in result


@pytest.mark.parametrize('input_data, expected', [
    ({'steps': ['Step 1'], 'parameters': {}}, 'success'),
    ({'steps': ['Invalid Step'], 'parameters': {}}, 'failure'),
])
def test_execute_task_parametrized(input_data, expected):
    """Parameterized test for task execution with different inputs."""
    result = execute_task(input_data)
    assert result['status'] == expected
