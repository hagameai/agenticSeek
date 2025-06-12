# agent_utilities.py

"""
Utility functions for managing agents in the AgenticSeek project.
These functions help in creating, retrieving, updating, and deleting agents.
"""

from typing import List, Dict, Any, Optional

class Agent:
    def __init__(self, name: str, agent_type: str, capabilities: List[str]):
        """
        Initialize an agent with a name, type, and capabilities.
        :param name: The name of the agent.
        :param agent_type: The type of the agent (e.g., 'browser', 'code').
        :param capabilities: A list of capabilities the agent has.
        """
        self.name = name
        self.agent_type = agent_type
        self.capabilities = capabilities

    def __repr__(self):
        return f"Agent(name={self.name}, type={self.agent_type}, capabilities={self.capabilities})"

class AgentManager:
    def __init__(self):
        """
        Initialize the AgentManager with an empty list of agents.
        """
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """
        Add a new agent to the manager.
        :param agent: The agent to be added.
        """
        self.agents.append(agent)

    def remove_agent(self, name: str) -> bool:
        """
        Remove an agent by name.
        :param name: The name of the agent to remove.
        :return: True if the agent was removed, False if not found.
        """
        for i, agent in enumerate(self.agents):
            if agent.name == name:
                del self.agents[i]
                return True
        return False

    def get_agent(self, name: str) -> Optional[Agent]:
        """
        Retrieve an agent by name.
        :param name: The name of the agent to retrieve.
        :return: The agent if found, None otherwise.
        """
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None

    def list_agents(self) -> List[Dict[str, Any]]:
        """
        List all agents with their details.
        :return: A list of dictionaries containing agent details.
        """
        return [vars(agent) for agent in self.agents]

# Example usage:
# manager = AgentManager()
# manager.add_agent(Agent('BrowserAgent', 'browser', ['navigate', 'scrape']))
# print(manager.list_agents())