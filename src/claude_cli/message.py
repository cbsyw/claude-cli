
# src/claude_cli/message.py
from dataclasses import dataclass
from typing import List, Dict
import anthropic

@dataclass
class Message:
   role: str
   content: str

class MessageHandler:
   def __init__(self, config):
       self.config = config
       self.history: List[Message] = []

   def add_message(self, message: Message) -> None:
       self.history.append(message)

   def get_messages(self) -> List[Dict[str, str]]:
       return [{"role": msg.role, "content": msg.content} for msg in self.history]

   async def send_message(self, content: str) -> str:
       self.add_message(Message(role="user", content=content))
       response = await self.config.client.messages.create(
           model=self.config.model,
           max_tokens=self.config.max_tokens,
           messages=self.get_messages()
       )
       self.add_message(Message(role="assistant", content=response.content))
       return response.content
