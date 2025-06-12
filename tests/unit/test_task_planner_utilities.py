import unittest
from src.utils.task_utils import TaskPlanner  # Assuming TaskPlanner is the class under test

class TestTaskPlannerUtilities(unittest.TestCase):
    def setUp(self):
        # Setup any necessary state here
        self.planner = TaskPlanner()  # Initialize the task planner

    def test_split_task_into_steps(self):
        # Test task splitting functionality
        task = 'Complete the project documentation'
        expected_steps = ['Write introduction', 'Document API', 'Review and edit']
        actual_steps = self.planner.split_task_into_steps(task)
        self.assertEqual(actual_steps, expected_steps)

    def test_estimate_task_duration(self):
        # Test duration estimation functionality
        steps = ['Write introduction', 'Document API', 'Review and edit']
        expected_duration = 5  # Assuming it takes 5 hours total
        actual_duration = self.planner.estimate_task_duration(steps)
        self.assertEqual(actual_duration, expected_duration)

    def test_handle_empty_task(self):
        # Test how function handles an empty task
        task = ''
        with self.assertRaises(ValueError):
            self.planner.split_task_into_steps(task)

    def test_handle_invalid_steps(self):
        # Test how function handles invalid steps
        with self.assertRaises(TypeError):
            self.planner.estimate_task_duration(None)

if __name__ == '__main__':
    unittest.main()