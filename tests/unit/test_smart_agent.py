import unittest
from src.agents.smart_agent import SmartAgent


class TestSmartAgent(unittest.TestCase):
    def setUp(self):
        """Set up test case environment"""
        self.agent = SmartAgent()  # Initialize the SmartAgent for testing

    def test_agent_initialization(self):
        """Test if the SmartAgent initializes correctly"""
        self.assertIsNotNone(self.agent, "SmartAgent should be initialized!")
        self.assertEqual(self.agent.state, 'idle', "Agent should start in idle state!")

    def test_agent_functionality(self):
        """Test the core functionality of the SmartAgent"""
        result = self.agent.perform_task('sample task')
        self.assertTrue(result, "Agent should successfully perform the task!")

    def test_agent_error_handling(self):
        """Test the error handling of SmartAgent"""
        with self.assertRaises(ValueError):
            self.agent.perform_task(None)  # Expecting ValueError when task is None

    def tearDown(self):
        """Clean up after tests"""
        self.agent = None


if __name__ == '__main__':
    unittest.main()