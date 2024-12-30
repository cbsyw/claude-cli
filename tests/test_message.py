

# tests/test_message.py
import pytest
from claude_cli.message import Message, MessageHandler
from claude_cli.config import Config

@pytest.fixture
def config():
   return Config(api_key="test_key")

@pytest.fixture
def handler(config):
   return MessageHandler(config)

def test_message_creation():
   msg = Message(role="user", content="test")
   assert msg.role == "user"
   assert msg.content == "test"

def test_handler_history(handler):
   msg = Message(role="user", content="test")
   handler.add_message(msg)
   assert len(handler.history) == 1
   assert handler.history[0].content == "test"

def test_get_messages(handler):
   handler.add_message(Message(role="user", content="Q1"))
   handler.add_message(Message(role="assistant", content="A1"))
   messages = handler.get_messages()
   assert len(messages) == 2
