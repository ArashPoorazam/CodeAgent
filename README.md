Here's a professional README for the CodeAgent project:

# CodeAgent

An AI-powered code assistant that uses Google's Gemini API to help developers analyze, debug, and modify code through natural language commands.

## Overview

CodeAgent is a command-line tool that leverages function calling capabilities of Google's Gemini 2.0 Flash model to interact with your codebase. It can read files, list directories, execute Python scripts, and write code modifications based on conversational prompts.

## Features

- **Natural Language Interface**: Ask questions about your code in plain English
- **File Operations**: Read, write, and analyze files in your project
- **Code Execution**: Run Python files and capture their output
- **Directory Navigation**: List and explore project structure
- **Iterative Problem Solving**: Agent can make multiple function calls to complete complex tasks
- **Verbose Mode**: Optional detailed logging of API usage and function calls
- **Safety Constraints**: All operations are restricted to the working directory

## Requirements

- Python 3.x
- Google Gemini API key
- Dependencies:
  - `google-genai`
  - `python-dotenv`

## Installation

1. Clone the repository:
```bash
git clone github.com/ArashPoorazam/CodeAgent
cd CodeAgent

2. Install dependencies:
bash
pip install google-genai python-dotenv

3. Create a `.env` file in the project root:
bash
GEMINI_API_KEY=your_api_key_here

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage

Basic usage:
bash
python main.py "your prompt here"

With verbose output:
bash
python main.py "your prompt here" --verbose

### Example Commands

Analyze code:
bash
python main.py "What does the calculator.py file do?"

Debug issues:
bash
python main.py "Why is my calculator returning wrong results?"

Modify code:
bash
python main.py "Add error handling to the divide function"

Run tests:
bash
python main.py "Run the test file and tell me what failed"

## Available Functions

The agent has access to four core functions:

### 1. `get_files_info`
Lists files and directories with their sizes.
python
# Example: "Show me all files in the src directory"

### 2. `get_file_content`
Reads and returns file content (up to 10,000 characters by default).
python
# Example: "Read the main.py file"

### 3. `run_python_file`
Executes Python files and captures stdout/stderr.
python
# Example: "Run calculator.py with arguments 5 and 3"

### 4. `write_file`
Creates or overwrites files with new content.
python
# Example: "Fix the bug in utils.py"

## Project Structure


.
├── main.py                  # Entry point and main loop
├── call_function.py         # Function dispatcher
├── config.py                # Configuration (MAX_ITERS, MAX_CHARS)
├── prompts.py               # System prompt for the agent
├── functions/
│   ├── get_file_content.py  # File reading function
│   ├── get_files_info.py    # Directory listing function
│   ├── run_python_file.py   # Python execution function
│   └── write_file.py        # File writing function
└── .env                     # API key (not committed)

## Configuration

Edit `config.py` to adjust:
- `MAX_ITERS`: Maximum number of agent iterations (default: 10)
- `MAX_CHARS`: Maximum characters to read from files (default: 10,000)

## How It Works

1. **User Input**: You provide a natural language prompt
2. **Agent Processing**: Gemini analyzes the request and decides which functions to call
3. **Function Execution**: The agent calls available functions (read files, run code, etc.)
4. **Iterative Refinement**: Agent can make multiple function calls to gather information
5. **Final Response**: Agent synthesizes results and provides a natural language answer

## Safety Features

- **Directory Sandboxing**: All file operations are restricted to the working directory
- **Path Validation**: Prevents directory traversal attacks
- **Execution Timeout**: Python scripts timeout after 30 seconds
- **File Size Limits**: Large files are truncated to prevent memory issues
- **Error Handling**: Graceful error messages for invalid operations

## Limitations

- Only executes Python files (`.py` extension required)
- File reading limited to `MAX_CHARS` characters
- Script execution timeout of 30 seconds
- All operations must be within the working directory

## Example Session

bash
$ python main.py "What files are in this project?"

Final response:
This project contains the following files:
- main.py: The entry point that handles user input
- call_function.py: Dispatches function calls to appropriate handlers
- config.py: Configuration settings
- prompts.py: System instructions for the AI agent
- Four function modules in the functions/ directory

$ python main.py "Run calculator.py and tell me if it works" --verbose

User prompt: Run calculator.py and tell me if it works

Prompt tokens: 1247
Response tokens: 89
-> STDOUT:
5 + 3 = 8
5 - 3 = 2
...

Final response:
The calculator.py file runs successfully and performs basic arithmetic operations correctly.

## Contributing

This project is part of the [boot.dev](https://boot.dev) curriculum. Feel free to fork and extend with additional functions or capabilities.

## License

Educational project from boot.dev.

## Acknowledgments

- Built with Google's Gemini 2.0 Flash API
- Part of the boot.dev AI Engineering course


This README provides comprehensive documentation for the CodeAgent project based on the code structure you provided.
