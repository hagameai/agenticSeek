import unittest
from src.utils.task_utils import split_task, execute_task

class TestTaskPlannerUtilities(unittest.TestCase):
    def test_split_task_valid(self):
        task = "Prepare a presentation"
        expected = ["Prepare", "a", "presentation"]
        result = split_task(task)
        self.assertEqual(result, expected)

    def test_split_task_empty(self):
        task = ""
        expected = []
        result = split_task(task)
        self.assertEqual(result, expected)

    def test_execute_task_success(self):
        task = "Prepare a presentation"
        result = execute_task(task)
        self.assertTrue(result)

    def test_execute_task_failure(self):
        task = None
        with self.assertRaises(ValueError):
            execute_task(task)

if __name__ == '__main__':
    unittest.main()