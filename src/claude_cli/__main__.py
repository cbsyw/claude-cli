
# src/claude_cli/__main__.py
import asyncio
import sys
from .main import main

def run_cli():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    run_cli()
