import unittest
from src.interaction import TaskPlanner, Task


class TestTaskPlanner(unittest.TestCase):
    def setUp(self):
        self.task_planner = TaskPlanner()

    def test_create_task(self):
        task = Task(name='Test Task', description='A simple test task')
        self.task_planner.create_task(task)
        self.assertIn(task, self.task_planner.tasks)

    def test_execute_task(self):
        task = Task(name='Test Task', description='A simple test task')
        self.task_planner.create_task(task)
        result = self.task_planner.execute_task(task)
        self.assertEqual(result, 'Task executed successfully')

    def test_split_complex_task(self):
        complex_task = Task(name='Complex Task', description='A complex task that needs splitting')
        self.task_planner.create_task(complex_task)
        sub_tasks = self.task_planner.split_complex_task(complex_task)
        self.assertTrue(len(sub_tasks) > 0)
        for sub_task in sub_tasks:
            self.assertIsInstance(sub_task, Task)

    def test_handle_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.task_planner.execute_task(Task(name='Nonexistent Task'))


if __name__ == '__main__':
    unittest.main()