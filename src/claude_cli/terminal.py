
# src/claude_cli/terminal.py
import readline
import os
from typing import Optional
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress
from rich.theme import Theme

class TerminalUI:
   def __init__(self):
       self.theme = Theme({
           "user": "green",
           "assistant": "blue",
           "error": "red bold"
       })
       self.console = Console(theme=self.theme)
       self.setup_history()

   def setup_history(self):
       self.history_file = os.path.expanduser('~/.claude_history')
       readline.set_history_length(1000)
       try:
           readline.read_history_file(self.history_file)
       except FileNotFoundError:
           pass

   def save_history(self):
       readline.write_history_file(self.history_file)

   def display_response(self, text: str):
       with Progress() as progress:
           task = progress.add_task("Processing...", total=100)
           self.console.print(Markdown(text), style="assistant")
           progress.update(task, completed=100)

   def clear_screen(self):
       os.system('clear' if os.name == 'posix' else 'cls')

   def get_input(self, prompt: str = "[user]You:[/] ") -> Optional[str]:
       try:
           return input(self.console.render(prompt)).strip()
       except (KeyboardInterrupt, EOFError):
           return None

   def display_error(self, error: str):
       self.console.print(f"Error: {error}", style="error")
