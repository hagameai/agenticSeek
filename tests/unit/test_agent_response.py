import unittest
from src.agents.advanced_agent import AdvancedAgent

class TestAgentResponse(unittest.TestCase):
    def setUp(self):
        # Set up the AdvancedAgent before each test
g        self.agent = AdvancedAgent()

    def test_agent_response_valid_input(self):
        # Test the agent's response to valid input
        user_input = "What is the capital of France?"
        expected_output = "The capital of France is Paris."
        response = self.agent.get_response(user_input)
        self.assertEqual(response, expected_output)

    def test_agent_response_invalid_input(self):
        # Test the agent's response to invalid input
        user_input = ""
        expected_output = "Sorry, I didn't understand that."
        response = self.agent.get_response(user_input)
        self.assertEqual(response, expected_output)

    def test_agent_response_edge_case(self):
        # Test the agent's response to an edge case
        user_input = "Tell me a joke."
        expected_output = "Why did the chicken cross the road? To get to the other side!"
        response = self.agent.get_response(user_input)
        self.assertEqual(response, expected_output)

if __name__ == '__main__':
    unittest.main()