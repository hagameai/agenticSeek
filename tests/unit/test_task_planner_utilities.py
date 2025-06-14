import unittest
from src.utils.task_utils import split_task_into_steps, validate_task_steps

class TestTaskPlannerUtilities(unittest.TestCase):
    def test_split_task_into_steps(self):
        # Test that the function correctly splits a simple task string into steps.
        task = "Write a report"
        expected_steps = ["Write the introduction", "Gather data", "Analyze data", "Write the conclusion"]
        actual_steps = split_task_into_steps(task)
        self.assertEqual(actual_steps, expected_steps)

    def test_invalid_task_string(self):
        # Test that an invalid task string raises a ValueError.
        with self.assertRaises(ValueError):
            split_task_into_steps("")

    def test_validate_task_steps(self):
        # Test that valid steps return True.
        steps = ["Step 1: Gather information", "Step 2: Analyze data"]
        self.assertTrue(validate_task_steps(steps))

    def test_invalid_task_steps(self):
        # Test that an invalid step raises a ValueError.
        steps = ["Step 1: ", "Step 2: Analyze data"]
        with self.assertRaises(ValueError):
            validate_task_steps(steps)

if __name__ == '__main__':
    unittest.main()