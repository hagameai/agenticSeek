import unittest
from src.api.task_api import TaskPlanner  # Assuming TaskPlanner is the class responsible for task execution logic

class TestTaskExecution(unittest.TestCase):
    def setUp(self):
        self.planner = TaskPlanner()  # Initialize TaskPlanner before each test

    def test_task_execution_success(self):
        task = "Complete the report"
        expected_result = "Report completed successfully"
        result = self.planner.execute_task(task)
        self.assertEqual(result, expected_result, "Task should execute successfully")

    def test_task_execution_failure(self):
        task = "Invalid task"
        expected_result = "Error: Task cannot be executed"
        result = self.planner.execute_task(task)
        self.assertEqual(result, expected_result, "Invalid task should not execute")

    def test_task_execution_with_dependencies(self):
        task = "Prepare presentation"
        dependencies = ["Gather data", "Create slides"]
        self.planner.add_dependencies(task, dependencies)
        result = self.planner.execute_task(task)
        self.assertIn("Presentation prepared successfully", result, "Task with dependencies should execute correctly")

    def test_task_execution_edge_cases(self):
        task = ""
        expected_result = "Error: Task description is empty"
        result = self.planner.execute_task(task)
        self.assertEqual(result, expected_result, "Empty task should not execute")

if __name__ == '__main__':
    unittest.main()