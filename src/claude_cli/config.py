

# src/claude_cli/config.py
from typing import Optional
import os
from pathlib import Path
from dotenv import load_dotenv
import anthropic

class Config:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or self._load_api_key()
        self.client = anthropic.Client(api_key=self.api_key)
        self.model = "claude-3-sonnet-20240229"
        self.max_tokens = 4096
        self.history_file = Path.home() / ".claude_history"

    def _load_api_key(self) -> str:
        load_dotenv()
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment or .env file")
        return api_key

    def get_client(self) -> anthropic.Client:
        return self.client
