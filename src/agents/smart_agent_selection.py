import random

class SmartAgentSelector:
    """
    This class is responsible for selecting the best agent based on user input and task requirements.
    """

    def __init__(self, agents):
        """
        Initialize the selector with a list of available agents.
        
        :param agents: List of agent instances.
        """
        self.agents = agents

    def select_agent(self, user_input):
        """
        Select the best agent based on the user's input.
        The selection logic can be enhanced based on task complexity and agent capabilities.
        
        :param user_input: User's request or query to determine the best agent.
        :return: Selected agent instance.
        """
        # Here we can implement a simple logic based on keywords
        # This is a placeholder for more complex logic
        selected_agent = random.choice(self.agents)
        return selected_agent

# Example usage
if __name__ == '__main__':
    from sources.agents.browser_agent import BrowserAgent
    from sources.agents.coder_agent import CoderAgent

    agents = [BrowserAgent(), CoderAgent()]
    selector = SmartAgentSelector(agents)
    user_input = "Write a Python script to fetch data from an API."
    selected_agent = selector.select_agent(user_input)
    print(f'Selected agent: {selected_agent.__class__.__name__}')