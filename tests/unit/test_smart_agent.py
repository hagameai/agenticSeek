import unittest
from src.agents.smart_agent import SmartAgent

class TestSmartAgent(unittest.TestCase):
    def setUp(self):
        """Initialize a SmartAgent instance for testing."""
        self.agent = SmartAgent(name="TestAgent")

    def test_agent_initialization(self):
        """Test that the SmartAgent initializes with the correct name."""
        self.assertEqual(self.agent.name, "TestAgent")

    def test_agent_task_execution(self):
        """Test that the SmartAgent can execute a given task."""
        task = "Write a sample code."
        result = self.agent.execute_task(task)
        self.assertIsNotNone(result)
        self.assertIn("code", result)

    def test_agent_response_generation(self):
        """Test that the SmartAgent generates appropriate responses."""
        response = self.agent.generate_response("What is AI?")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

    def tearDown(self):
        """Clean up after each test case."""
        del self.agent

if __name__ == '__main__':
    unittest.main()