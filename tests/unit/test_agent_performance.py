import unittest
from sources.agents.agent import Agent  # Assuming Agent class exists in this path


class TestAgentPerformance(unittest.TestCase):
    """
    Unit tests for agent performance metrics
    """

    def setUp(self):
        """
        Create an instance of the Agent for testing
        """  
        self.agent = Agent()  # Initialize your agent here

    def test_performance_metric_accuracy(self):
        """
        Test if the agent's performance metric accuracy is within acceptable range
        """
        expected_accuracy = 0.95  # Define acceptable accuracy
        actual_accuracy = self.agent.get_performance_metric('accuracy')  # Assuming this method exists
        self.assertGreaterEqual(actual_accuracy, expected_accuracy,
            f'Expected accuracy >= {expected_accuracy}, but got {actual_accuracy}') 

    def test_performance_metric_response_time(self):
        """
        Test if the agent's response time is within acceptable limits
        """
        max_response_time = 2.0  # Define max acceptable response time in seconds
        response_time = self.agent.get_performance_metric('response_time')  # Assuming this method exists
        self.assertLessEqual(response_time, max_response_time,
            f'Expected response time <= {max_response_time}, but got {response_time}') 

    def tearDown(self):
        """
        Clean up after tests
        """
        del self.agent  # Clean up the agent instance


if __name__ == '__main__':
    unittest.main()