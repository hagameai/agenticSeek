import unittest
from src.utils.agent_interaction_utils import some_utility_function


class TestAgentInteractionUtils(unittest.TestCase):
    def test_some_utility_function(self):
        # Test case for the utility function
        input_data = "input"
        expected_output = "expected_output"
        result = some_utility_function(input_data)
        self.assertEqual(result, expected_output)

    def test_some_utility_function_with_edge_case(self):
        # Test case for an edge case
        input_data = "edge_case_input"
        expected_output = "edge_case_expected_output"
        result = some_utility_function(input_data)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()