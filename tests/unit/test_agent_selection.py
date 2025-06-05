import unittest
from src.agents.advanced_agent import AdvancedAgent

class TestSmartAgentSelection(unittest.TestCase):
    def setUp(self):
        """Set up the test case with an instance of AdvancedAgent."""
        self.agent = AdvancedAgent()

    def test_agent_selection_valid_task(self):
        """Test smart agent selection for a valid task."""
        task = 'coding'
        selected_agent = self.agent.select_agent(task)
        self.assertIsNotNone(selected_agent, "Agent should be selected for valid task")
        self.assertEqual(selected_agent.task_type, task, "Selected agent should match the task type")

    def test_agent_selection_invalid_task(self):
        """Test smart agent selection for an invalid task."""
        task = 'unknown_task'
        selected_agent = self.agent.select_agent(task)
        self.assertIsNone(selected_agent, "No agent should be selected for invalid task")

    def test_agent_selection_edge_case(self):
        """Test smart agent selection with edge case input."""
        task = ''  # empty task
        selected_agent = self.agent.select_agent(task)
        self.assertIsNone(selected_agent, "No agent should be selected for empty task")

if __name__ == '__main__':
    unittest.main()