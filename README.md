# Multi-Agent Collaborative System

This project implements a multi-agent collaborative system using the Google Agent Development Kit (ADK). The system consists of a master agent that delegates tasks to specialized agents for file operations, web browsing, and terminal commands.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   To run the agentic pipeline, execute the `main.py` script with a request:
   ```bash
   python main.py "Your request here"
   ```
   For example:
   ```bash
   python main.py "What is the weather in New York?"
   ```

## Running Tests

To run the unit tests, use the following command:
```bash
python -m unittest discover tests
```
