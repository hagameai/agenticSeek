# task_utils.py
# Utility functions for task management in AgenticSeek project.

from typing import List, Dict, Any


def split_task_into_steps(task: str) -> List[str]:
    """
    Splits a complex task into manageable steps.
    
    Parameters:
    - task (str): The complex task to be split.
    
    Returns:
    - List[str]: A list of manageable steps.
    """
    # Basic implementation: Splitting by commas as a simple example
    steps = task.split(',')
    return [step.strip() for step in steps]


def create_task_report(steps: List[str]) -> Dict[str, Any]:
    """
    Creates a report of the task with its steps.
    
    Parameters:
    - steps (List[str]): The steps of the task.
    
    Returns:
    - Dict[str, Any]: A dictionary report with task details.
    """
    report = {
        'total_steps': len(steps),
        'steps': steps,
        'status': 'Pending'
    }
    return report


def mark_task_completed(report: Dict[str, Any]) -> None:
    """
    Marks the task as completed in the report.
    
    Parameters:
    - report (Dict[str, Any]): The task report to update.
    """
    report['status'] = 'Completed'

