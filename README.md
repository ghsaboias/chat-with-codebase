# Codebase Analyzer with Claude AI

This project provides a set of tools to analyze and interact with a codebase using Claude AI. It consists of three main components:

1. A script to extract and compile codebase contents
2. A chat interface to interact with Claude AI about the codebase
3. A requirements file listing all necessary dependencies

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Extracting Codebase Contents](#extracting-codebase-contents)
  - [Chatting with Claude AI](#chatting-with-claude-ai)
- [File Descriptions](#file-descriptions)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/ghsaboias/prompt-caching.git
   cd codebase-analyzer
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
   python get_codebase.py
   ```

2. When prompted, enter the path to the directory containing your codebase, or press Enter to use the current directory.

3. Optionally, specify an output file name, or press Enter to use the default `output.txt`.

The script will create a single file containing the contents of all code files in the specified directory, ignoring certain files and directories (like `.git`, `node_modules`, etc.).

### Chatting with Claude AI

1. Ensure you have run `get_codebase.py` and have an `output.txt` file containing your codebase.

2. Run the chat script:

   ```
   python chat_with_cache.py
   ```

3. Enter your questions or comments about the codebase when prompted. Type 'exit' to end the conversation.

Claude AI will analyze the codebase and respond to your queries, providing insights and explanations based on the code contents.

## File Descriptions

- `get_codebase.py`: Script to extract and compile codebase contents into a single file.
- `chat_with_cache.py`: Script to interact with Claude AI about the codebase.
- `requirements.txt`: List of Python package dependencies.
- `output.txt`: Generated file containing the compiled codebase contents (not included in repository).

## Dependencies

This project relies on several Python packages, including:

- anthropic
- beautifulsoup4
- requests
- pydantic
- huggingface-hub

For a complete list of dependencies and their versions, refer to the `requirements.txt` file.

## Configuration

- The `chat_with_cache.py` script uses the Claude 3 Sonnet model (`claude-3-5-sonnet-20240620`). You can modify the `MODEL_NAME` variable in the script to use a different model if desired.
- The script uses prompt caching to improve performance. This is configured with the `extra_headers` parameter in the API call.

## Troubleshooting

- If you encounter issues reading the `output.txt` file, ensure it exists in the same directory as the `chat_with_cache.py` script.
- Make sure your Anthropic API key is correctly set as an environment variable.
- If you experience rate limiting or other API-related issues, check your Anthropic account status and API usage limits.

## Contributing

Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
