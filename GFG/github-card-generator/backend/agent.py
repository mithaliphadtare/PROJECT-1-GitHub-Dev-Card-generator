from adk.agent import Agent
from adk.event import Event
from adk.message import Message

class GitHubDevCardAgent(Agent):
    def __init__(self):
        super().__init__()
        self.register_event_handler("github.devcard.generate", self.handle_generate_dev_card)

    async def handle_generate_dev_card(self, event: Event):
        # Agent logic to generate a GitHub Dev Card
        message = Message(
            payload={"card_data": "Generated Dev Card Data"},
            event_id=event.event_id,
        )
        await self.send_message(message)

def create_agent():
    return GitHubDevCardAgent()

if __name__ == "__main__":
    agent = create_agent()
    agent.run()
