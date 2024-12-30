

# src/claude_cli/main.py
import asyncio
from .config import Config
from .message import MessageHandler
from .terminal import TerminalUI

async def main(terminal=None, handler=None):
    if not terminal:
        terminal = TerminalUI()
    if not handler:
        config = Config()
        handler = MessageHandler(config)

    while True:
        user_input = terminal.get_input()
        if not user_input:
            break

        try:
            response = await handler.send_message(user_input)
            terminal.display_response(response)
        except Exception as e:
            terminal.display_error(str(e))

if __name__ == "__main__":
    asyncio.run(main())
