
# tests/test_main.py
import pytest
from unittest.mock import AsyncMock, MagicMock
from claude_cli.main import main

@pytest.fixture
def mock_terminal():
   terminal = MagicMock()
   terminal.get_input.side_effect = ["test input", None]
   return terminal

@pytest.fixture
def mock_handler():
   handler = MagicMock()
   handler.send_message = AsyncMock(return_value="test response")
   return handler

@pytest.mark.asyncio
async def test_main_loop(mock_terminal, mock_handler):
   await main(terminal=mock_terminal, handler=mock_handler)
   assert mock_terminal.get_input.called
   assert mock_handler.send_message.called
   mock_terminal.display_response.assert_called_with("test response")
