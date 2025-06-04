import unittest
from src.agents.smart_agent_selection import select_best_agent


class TestSmartAgentSelection(unittest.TestCase):
    def setUp(self):
        # Setup any necessary data or state before each test
        self.user_input = 'I need to code a Python script.'
        self.agents = [
            {'name': 'CodeAgent', 'capabilities': ['coding']},
            {'name': 'BrowserAgent', 'capabilities': ['browsing']},
            {'name': 'PlannerAgent', 'capabilities': ['planning']}
        ]

    def test_select_best_agent_for_coding(self):
        # Test for selecting the best agent based on user input
        best_agent = select_best_agent(self.user_input, self.agents)
        self.assertEqual(best_agent['name'], 'CodeAgent', 'The best agent should be the CodeAgent for coding tasks.')

    def test_select_best_agent_for_browsing(self):
        # Test for browsing input
        self.user_input = 'Find the latest news on AI.'
        best_agent = select_best_agent(self.user_input, self.agents)
        self.assertEqual(best_agent['name'], 'BrowserAgent', 'The best agent should be the BrowserAgent for browsing tasks.')

    def test_select_best_agent_for_planning(self):
        # Test for planning input
        self.user_input = 'Help me plan my day.'
        best_agent = select_best_agent(self.user_input, self.agents)
        self.assertEqual(best_agent['name'], 'PlannerAgent', 'The best agent should be the PlannerAgent for planning tasks.')

    def tearDown(self):
        # Clean up after each test if necessary
        pass


if __name__ == '__main__':
    unittest.main()