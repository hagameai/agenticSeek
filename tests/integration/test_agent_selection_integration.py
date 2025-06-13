import unittest
from src.agents.smart_agent import SmartAgent

class TestSmartAgentSelectionIntegration(unittest.TestCase):
    def setUp(self):
        # Initialize SmartAgent before each test
        self.agent = SmartAgent()

    def test_agent_selection_for_browsing(self):
        # Test the agent selection for a browsing task
        result = self.agent.select_agent(task_type='browsing')
        self.assertIsNotNone(result, "Agent should be selected for browsing task")
        self.assertEqual(result.name, 'BrowserAgent', "Selected agent should be BrowserAgent")

    def test_agent_selection_for_coding(self):
        # Test the agent selection for a coding task
        result = self.agent.select_agent(task_type='coding')
        self.assertIsNotNone(result, "Agent should be selected for coding task")
        self.assertEqual(result.name, 'CodeAgent', "Selected agent should be CodeAgent")

    def test_agent_selection_for_planning(self):
        # Test the agent selection for a planning task
        result = self.agent.select_agent(task_type='planning')
        self.assertIsNotNone(result, "Agent should be selected for planning task")
        self.assertEqual(result.name, 'PlannerAgent', "Selected agent should be PlannerAgent")

    def tearDown(self):
        # Clean up resources after each test
        self.agent = None

if __name__ == '__main__':
    unittest.main()