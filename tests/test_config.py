
# tests/test_config.py
import pytest
import os
from claude_cli.config import Config

def test_api_key_from_env():
   os.environ["ANTHROPIC_API_KEY"] = "test_key"
   config = Config()
   assert config.api_key == "test_key"

def test_api_key_direct():
   config = Config(api_key="direct_key")
   assert config.api_key == "direct_key"

def test_no_api_key():
   if "ANTHROPIC_API_KEY" in os.environ:
       del os.environ["ANTHROPIC_API_KEY"]
   with pytest.raises(ValueError):
       Config()

def test_client_creation():
   config = Config(api_key="test_key")
   assert config.get_client() is not None
