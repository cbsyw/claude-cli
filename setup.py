
# setup.py
from setuptools import setup, find_packages

setup(
   name="claude-cli",
   version="0.1.0",
   packages=find_packages(where="src"),
   package_dir={"": "src"},
   install_requires=[
       "anthropic",
       "python-dotenv",
       "rich"
   ],
   entry_points={
       'console_scripts': [
           'claude=claude_cli.__main__:run_cli',
       ],
   },
)
