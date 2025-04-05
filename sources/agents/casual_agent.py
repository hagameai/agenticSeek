
from sources.utility import pretty_print, animate_thinking
from sources.agents.agent import Agent
from sources.tools.searxSearch import searxSearch
from sources.tools.flightSearch import FlightSearch
from sources.tools.fileFinder import FileFinder
from sources.tools.BashInterpreter import BashInterpreter

class CasualAgent(Agent):
    def __init__(self, name, prompt_path, provider, verbose=False):
        """
        The casual agent is a special for casual talk to the user without specific tasks.
        """
        super().__init__(name, prompt_path, provider, verbose, None)
        self.tools = {
        } # No tools for the casual agent
        self.role = {
            "en": "talk",
            "fr": "discuter",
            "zh": "聊天",
        }
        self.type = "casual_agent"
    
    def process(self, prompt, speech_module) -> str:
        self.memory.push('user', prompt)
        animate_thinking("Thinking...", color="status")
        answer, reasoning = self.llm_request()
        self.last_answer = answer
        return answer, reasoning

if __name__ == "__main__":
    pass