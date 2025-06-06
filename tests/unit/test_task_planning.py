import unittest
from src.interaction import TaskPlanner
from src.memory import Memory


class TestTaskPlanning(unittest.TestCase):
    def setUp(self):
        # Set up the necessary components for testing
        self.memory = Memory()
        self.task_planner = TaskPlanner(self.memory)

    def test_task_execution_single_step(self):
        # Test a single step task execution
        task = "Write a Python function."
        self.task_planner.add_task(task)
        result = self.task_planner.execute_tasks()
        self.assertIn("Function written successfully", result)

    def test_task_execution_multiple_steps(self):
        # Test execution of multiple steps
        tasks = ["Plan a project", "Implement the project", "Review the project"]
        for task in tasks:
            self.task_planner.add_task(task)
        result = self.task_planner.execute_tasks()
        self.assertEqual(len(result), len(tasks))
        self.assertTrue(all("Task executed successfully" in res for res in result))

    def test_empty_task_execution(self):
        # Test execution when no tasks are added
        result = self.task_planner.execute_tasks()
        self.assertEqual(result, ["No tasks to execute."])

    def tearDown(self):
        # Clean up after each test
        self.task_planner.clear_tasks()


if __name__ == '__main__':
    unittest.main()