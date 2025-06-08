import unittest
from src.agents.smart_agent import SmartAgent
from src.agents.agent_registry import AgentRegistry

class TestSmartAgentSelection(unittest.TestCase):
    def setUp(self):
        """Set up for the tests."""
        self.agent_registry = AgentRegistry()
        self.agent = SmartAgent(self.agent_registry)

    def test_agent_selection_based_on_task(self):
        """Test that the correct agent is selected based on task."""
        task = "coding"
        selected_agent = self.agent.select_agent(task)
        self.assertEqual(selected_agent.name, "CodeAgent")

    def test_agent_selection_with_empty_registry(self):
        """Test agent selection when registry is empty."""
        self.agent_registry.clear()  # Clear any agents
        task = "coding"
        with self.assertRaises(ValueError):
            self.agent.select_agent(task)

    def test_agent_selection_for_non_existent_task(self):
        """Test agent selection for a task that does not exist."""
        task = "non_existent_task"
        selected_agent = self.agent.select_agent(task)
        self.assertIsNone(selected_agent,
                         "Expected None for non-existent task selection")

    def tearDown(self):
        """Clean up after each test."""
        self.agent_registry.clear()

if __name__ == '__main__':
    unittest.main()