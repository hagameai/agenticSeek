import pytest
from src.agents.agent import Agent
from src.sources.interaction import Interaction


@pytest.fixture(scope="module")
def setup_agents():
    """Set up agents for testing."""
    agent1 = Agent(name="Agent 1")
    agent2 = Agent(name="Agent 2")
    return agent1, agent2


def test_agent_interaction(setup_agents):
    """Test interaction between two agents."""
    agent1, agent2 = setup_agents
    interaction = Interaction(agent1, agent2)

    # Simulate an interaction between the agents
    response = interaction.simulate_interaction()

    # Assert that the interaction response is valid
    assert response is not None, "Response should not be None"
    assert "interaction completed" in response, "Response should indicate completed interaction"


def test_agent_response(setup_agents):
    """Test the response functionality of agents."""
    agent1, agent2 = setup_agents
    response1 = agent1.get_response("Hello")
    response2 = agent2.get_response("Hi there")

    # Assert that the agents provide valid responses
    assert response1 is not None, "Agent 1 response should not be None"
    assert response2 is not None, "Agent 2 response should not be None"
    assert "Hello" in response1, "Agent 1 should acknowledge the greeting"
    assert "Hi there" in response2, "Agent 2 should acknowledge the greeting"