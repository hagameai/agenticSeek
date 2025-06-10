import unittest
from src.utils.task_utils import TaskPlanner, TaskExecutionError

class TestTaskUtilities(unittest.TestCase):

    def setUp(self):
        # Set up any necessary test data or state before each test
        self.task_planner = TaskPlanner()

    def test_plan_simple_task(self):
        # Test planning a simple task
        task = "Write unit tests"
        steps = self.task_planner.plan_task(task)
        self.assertEqual(steps, ["Identify functions to test", "Write test cases", "Run tests", "Review results"],
                         "The task planner did not return the expected steps.")

    def test_plan_complex_task(self):
        # Test planning a complex task
        task = "Develop a new feature"
        steps = self.task_planner.plan_task(task)
        self.assertIn("Gather requirements", steps,
                      "Expected step 'Gather requirements' not found in the planned steps.")
        self.assertIn("Implement feature", steps,
                      "Expected step 'Implement feature' not found in the planned steps.")

    def test_execute_task_success(self):
        # Test executing a task successfully
        task = "Write documentation"
        success = self.task_planner.execute_task(task)
        self.assertTrue(success, "Task execution should succeed.")

    def test_execute_task_failure(self):
        # Test executing a task that fails
        task = "Invalid task"
        with self.assertRaises(TaskExecutionError):
            self.task_planner.execute_task(task)

    def tearDown(self):
        # Clean up any necessary state after each test
        pass

if __name__ == '__main__':
    unittest.main()