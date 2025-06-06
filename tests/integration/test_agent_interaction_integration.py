import pytest
from sources.interaction import AgentInteraction
from sources.agents.browser_agent import BrowserAgent
from sources.agents.coder_agent import CoderAgent

@pytest.fixture
def setup_agents():
    browser_agent = BrowserAgent()
    coder_agent = CoderAgent()
    return browser_agent, coder_agent


def test_agent_interaction(setup_agents):
    browser_agent, coder_agent = setup_agents

    # Simulate a task for the browser agent
    query = "Search for AI development trends"
    browser_response = browser_agent.perform_action(query)
    assert browser_response is not None, "Browser agent should return a response"

    # Simulate interaction with coder agent based on browser response
    code_request = f"Write a Python function to print the trends: {browser_response}"
    coder_response = coder_agent.perform_action(code_request)
    assert coder_response is not None, "Coder agent should return a response"
    assert "def " in coder_response, "Response should contain a function definition"

    # Check if the code can be executed and returns expected output
    exec_globals = {}
    exec(coder_response, exec_globals)
    assert "trends" in exec_globals, "Function should define a 'trends' variable"
