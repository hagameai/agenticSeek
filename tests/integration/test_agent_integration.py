import unittest
from src.agents.advanced_agent import AdvancedAgent
from src.interaction import Interaction

class TestAgentIntegration(unittest.TestCase):
    """
    Integration tests for agent interactions.
    """

    def setUp(self):
        """Initialize the AdvancedAgent and Interaction before each test."""
        self.agent = AdvancedAgent()
        self.interaction = Interaction()

    def test_agent_response_to_query(self):
        """Test if the agent responds correctly to a simple query."""
        query = "What is AI?"
        response = self.agent.process_query(query)
        self.assertIn("artificial intelligence", response.lower(),
                      "Agent response should contain 'artificial intelligence'")

    def test_interaction_with_agent(self):
        """Test the interaction process between user and agent."""
        user_input = "Plan a workout for me."
        expected_response = self.interaction.execute(user_input)
        self.assertIsInstance(expected_response, str, "Expected response should be a string")
        self.assertNotEqual(expected_response, '', "Response should not be empty")

    def tearDown(self):
        """Clean up after each test."""
        del self.agent 
        del self.interaction

if __name__ == '__main__':
    unittest.main()