class AgentManager:
    """
    Class to manage multiple AI agents.
    This class allows for adding, removing, and retrieving agents based on various criteria.
    """

    def __init__(self):
        """Initialize the AgentManager with an empty list of agents."""
        self.agents = []

    def add_agent(self, agent):
        """Add an agent to the manager.

        Args:
            agent (object): The agent object to be added.
        """
        if agent not in self.agents:
            self.agents.append(agent)
        else:
            raise ValueError("Agent already exists in the manager.")

    def remove_agent(self, agent):
        """Remove an agent from the manager.

        Args:
            agent (object): The agent object to be removed.
        """
        try:
            self.agents.remove(agent)
        except ValueError:
            raise ValueError("Agent not found in manager.")

    def get_agents(self):
        """Retrieve all agents managed by this manager.

        Returns:
            list: A list of agents.
        """
        return self.agents

    def find_agents_by_type(self, agent_type):
        """Retrieve agents of a specific type.

        Args:
            agent_type (str): The type of agent to search for.

        Returns:
            list: A list of agents matching the specified type.
        """
        return [agent for agent in self.agents if isinstance(agent, agent_type)]