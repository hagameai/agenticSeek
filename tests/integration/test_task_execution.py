import unittest
from src.interaction import TaskPlanner
from tests.unit.test_task_planner import MockTaskPlanner

class TestTaskExecution(unittest.TestCase):
    def setUp(self):
        # Set up a mock task planner for testing
        self.task_planner = MockTaskPlanner()

    def test_execute_simple_task(self):
        # Test executing a simple task
        task = "Write a report"
        result = self.task_planner.execute(task)
        self.assertEqual(result, "Report written successfully")

    def test_execute_complex_task(self):
        # Test executing a complex task
        tasks = ["Gather information", "Analyze data", "Write report"]
        results = self.task_planner.execute_complex(tasks)
        expected_results = ["Information gathered", "Data analyzed", "Report written successfully"]
        self.assertEqual(results, expected_results)

    def test_execute_invalid_task(self):
        # Test handling of an invalid task
        task = "Invalid task"
        with self.assertRaises(ValueError):
            self.task_planner.execute(task)

    def tearDown(self):
        # Clean up any resources if necessary
        pass

if __name__ == '__main__':
    unittest.main()