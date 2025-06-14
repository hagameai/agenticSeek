import unittest
from src.interaction import TaskPlanner  # Import the TaskPlanner class from the interaction module

class TestTaskPlanningIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the test case by initializing the TaskPlanner."""
        self.task_planner = TaskPlanner()

    def test_task_planning_basic(self):
        """Test basic task planning functionality."""
        tasks = ["Task 1", "Task 2", "Task 3"]
        planned_steps = self.task_planner.plan_tasks(tasks)
        expected_steps = ["Step 1 for Task 1", "Step 1 for Task 2", "Step 1 for Task 3"]  # Example expected output
        self.assertEqual(planned_steps, expected_steps, "The planned steps do not match the expected output.")

    def test_task_planning_with_complex_tasks(self):
        """Test task planning with complex tasks."""
        complex_tasks = ["Complex Task 1", "Complex Task 2"]
        planned_steps = self.task_planner.plan_tasks(complex_tasks)
        expected_steps = ["Step 1 for Complex Task 1", "Step 1 for Complex Task 2"]  # Example expected output
        self.assertEqual(planned_steps, expected_steps, "The planned steps for complex tasks do not match the expected output.")

    def test_empty_task_list(self):
        """Test task planning with an empty task list."""
        tasks = []
        planned_steps = self.task_planner.plan_tasks(tasks)
        self.assertEqual(planned_steps, [], "The planned steps should be empty for an empty task list.")

    def tearDown(self):
        """Clean up after each test case."""
        pass  # Optional - add cleanup code if necessary

if __name__ == '__main__':
    unittest.main()