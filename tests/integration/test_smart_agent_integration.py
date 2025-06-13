import pytest
from src.agents.smart_agent import SmartAgent

class TestSmartAgent:
    @pytest.fixture(scope="module")
    def smart_agent(self):
        """Fixture to create a SmartAgent instance for testing."""
        agent = SmartAgent()
        return agent

    def test_agent_initialization(self, smart_agent):
        """Test that the SmartAgent is initialized correctly."""
        assert smart_agent is not None
        assert isinstance(smart_agent, SmartAgent)

    def test_agent_functionality(self, smart_agent):
        """Test the core functionality of the SmartAgent."""
        result = smart_agent.perform_task("example task")
        assert result is not None
        assert "task completed" in result

    def test_agent_selection(self, smart_agent):
        """Test the agent selection logic based on tasks."""
        selected_agent = smart_agent.select_agent("coding task")
        assert selected_agent is not None
        assert "code_agent" in selected_agent.name

    def test_invalid_task(self, smart_agent):
        """Test handling of invalid tasks."""
        with pytest.raises(ValueError):
            smart_agent.perform_task("")

    def test_agent_feedback(self, smart_agent):
        """Test the feedback mechanism of the SmartAgent."""
        feedback = smart_agent.provide_feedback("good performance")
        assert feedback is True

# Run tests with: pytest tests/integration/test_smart_agent_integration.py