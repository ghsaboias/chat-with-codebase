# Codebase Unifier with Claude AI

This project provides a set of tools to analyze and interact with a codebase using Claude AI. It extracts the contents of a codebase into a single file and allows for interactive conversations about the code using Claude's advanced language model.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Extracting Codebase Contents](#extracting-codebase-contents)
  - [Chatting with Claude AI](#chatting-with-claude-ai)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Extract and compile codebase contents into a single file
- Interactive chat interface with Claude AI about the codebase
- Utilizes prompt caching for improved performance
- Displays token usage and API call time information

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/codebase-unifier.git
   cd codebase-unifier
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up your Anthropic API key as an environment variable:
   ```
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

### Extracting Codebase Contents

1. Run the `get_codebase.py` script:

   ```
   python utils/get_codebase.py
   ```

2. When prompted, enter the path to the directory containing your codebase, or press Enter to use the current directory.

3. Optionally, specify an output file name, or press Enter to use the default `output.txt`.

The script will create a single file containing the contents of all code files in the specified directory, ignoring certain files and directories (like `.git`, `node_modules`, etc.).

### Chatting with Claude AI

1. Ensure you have run `get_codebase.py` and have an `output.txt` file containing your codebase.

2. Run the main script:

   ```
   python -m src.main
   ```

3. Enter your questions or comments about the codebase when prompted. Type 'exit' to end the conversation.

Claude AI will analyze the codebase and respond to your queries, providing insights and explanations based on the code contents.

## Project Structure

- `src/`: Main source code directory
  - `__init__.py`: Package initializer
  - `claude_chat.py`: Handles interactions with the Claude API
  - `conversation_history.py`: Manages the conversation history
  - `main.py`: Main script to run the chat application
- `utils/`: Utility scripts
  - `__init__.py`: Package initializer
  - `get_codebase.py`: Script to extract and compile codebase contents
- `tests/`: Directory for test files (currently empty)
- `config.py`: Contains configuration variables
- `requirements.txt`: List of Python package dependencies
- `setup.py`: Setup script for the project
- `README.md`: This file, containing project documentation

## Dependencies

This project relies on several Python packages, including:

- anthropic
- pydantic
- httpx
- tqdm

For a complete list of dependencies and their versions, refer to the `requirements.txt` file.

## Configuration

- The `config.py` file contains the `MODEL_NAME` variable, currently set to `"claude-3-5-sonnet-20240620"`. You can modify this to use a different Claude model if desired.
- The chat functionality uses prompt caching to improve performance. This is configured with the `extra_headers` parameter in the API call within the `ClaudeChat` class.
