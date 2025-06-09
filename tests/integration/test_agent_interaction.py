import pytest
from src.agents.smart_agent import SmartAgent
from src.agents.advanced_agent import AdvancedAgent
from src.interaction import AgentInteraction


@pytest.fixture
def setup_agents():
    # Setup smart and advanced agents for testing
    smart_agent = SmartAgent()
    advanced_agent = AdvancedAgent()
    return smart_agent, advanced_agent


def test_agent_interaction(setup_agents):
    smart_agent, advanced_agent = setup_agents

    # Simulate input for both agents
    user_input = "What is the weather like today?"
    task_id = 1

    # Testing interaction between smart agent and advanced agent
    interaction = AgentInteraction(smart_agent, advanced_agent)
    response = interaction.handle_request(user_input, task_id)

    # Assert that response contains expected output
    assert response is not None, "Response should not be None"
    assert 'weather' in response.lower(), "Response should relate to weather"

    # Testing interaction with an invalid input
    invalid_input = ""
    invalid_response = interaction.handle_request(invalid_input, task_id)
    assert invalid_response is None, "Response should be None for invalid input"