import unittest
from src.utils.task_utils import split_task_into_steps, execute_task_steps

class TestTaskPlannerUtilities(unittest.TestCase):

    def test_split_task_into_steps(self):
        # Test for valid input
        task = "Prepare a presentation"
        expected_steps = ["Research topic", "Create slides", "Practice delivery"]
        self.assertEqual(split_task_into_steps(task), expected_steps)

        # Test for empty input
        task = ""
        expected_steps = []
        self.assertEqual(split_task_into_steps(task), expected_steps)

        # Test for non-standard task string
        task = "Write report"
        expected_steps = ["Gather data", "Analyze results", "Draft report", "Revise report"]
        self.assertEqual(split_task_into_steps(task), expected_steps)

    def test_execute_task_steps(self):
        # Test execution of valid steps
        steps = ["Gather data", "Analyze results", "Draft report"]
        results = execute_task_steps(steps)
        self.assertTrue(results)  # Assuming the function returns True for success

        # Test execution with no steps
        steps = []
        results = execute_task_steps(steps)
        self.assertFalse(results)  # Assuming the function returns False for no steps

if __name__ == '__main__':
    unittest.main()