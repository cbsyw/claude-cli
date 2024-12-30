

# tests/test_terminal.py
import pytest
from claude_cli.terminal import TerminalUI
from unittest.mock import patch

@pytest.fixture
def terminal():
    return TerminalUI()

def test_input_handling(terminal):
    with patch('builtins.input', return_value="test input"):
        assert terminal.get_input() == "test input"
