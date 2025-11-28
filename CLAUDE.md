# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PYTAI is an OpenAI and Python integration project that implements a simple command-line chatbot using the OpenAI API. The project demonstrates basic integration with OpenAI's GPT models through a conversational interface.

## Setup and Dependencies

### Required Dependencies
- `openai` - OpenAI Python client library
- `python-dotenv` (referenced in README as python-denv)

### Installation
```bash
pip install openai python-dotenv
```

### Environment Configuration
The application requires an `OPENAI_API_KEY` environment variable to be set:

**Linux/macOS:**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**Windows Command Prompt:**
```cmd
set OPENAI_API_KEY=your-api-key-here
```

**Alternative:** Create a `.env` file in the project root with:
```
OPENAI_API_KEY=your-api-key-here
```

## Running the Application

Execute the main chatbot script:
```bash
python openpy.py
```

The script will:
- Initialize an OpenAI client with the API key from environment variables
- Start an interactive loop where users can ask questions
- Use the GPT-3.5-turbo model (configurable to GPT-4)
- Exit when user types 'exit'

## Code Architecture

### Main Script: openpy.py

The application follows a simple single-file architecture:

- **Client Initialization** (lines 4-9): Creates an OpenAI client instance using environment variable for API key, with validation
- **Main Loop** (lines 11-35): Implements an interactive REPL that:
  - Accepts user input via stdin
  - Sends requests to OpenAI's chat completion API with system and user messages
  - Handles responses and errors
  - Continues until 'exit' command

### API Configuration
- Model: `gpt-3.5-turbo` (can be changed to `gpt-4`)
- Max tokens: 150
- Temperature: 0.7
- System prompt: "You are a helpful assistant."

## Key Implementation Details

- The script validates API key presence before proceeding (openpy.py:7-9)
- Uses the modern OpenAI Python client API with `client.chat.completions.create()`
- Implements basic error handling with try-except blocks
- Interactive session ends with "Press Enter to exit" for user convenience
