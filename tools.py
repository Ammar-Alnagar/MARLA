import os
import fnmatch
from typing import List

def local_file_search(directory: str, pattern: str) -> List[str]:
    """Searches for files matching a pattern within a specified directory.
    Args:
        directory (str): The directory to start the search from.
        pattern (str): The pattern to match filenames against (e.g., '*.py', 'document.txt').
    Returns:
        List[str]: A list of absolute paths to matching files.
    """
    matches = []
    for root, _, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

# Placeholder for other tools
# def local_file_edit(file_path: str, content: str):
#     pass

# def web_search(query: str):
#     pass

# def terminal_use(command: str):
#     pass




def local_file_edit(file_path: str, content: str):
    """Edits the content of a local file, overwriting its existing content.
    Args:
        file_path (str): The absolute path to the file to edit.
        content (str): The new content to write to the file.
    """
    with open(file_path, 'w') as f:
        f.write(content)
    return f"File {file_path} edited successfully."




import requests

def web_search(query: str) -> str:
    """Performs a web search and returns the top results.
    Args:
        query (str): The search query.
    Returns:
        str: A string containing the search results.
    """
    # This is a placeholder for a real web search API call.
    # For a real implementation, you would integrate with a search engine API (e.g., Google Custom Search API).
    return f"Simulated web search results for: {query}. (Actual search functionality not implemented)"




import subprocess
from memory import Memory

memory = Memory()

def terminal_use(command: str) -> str:
    """Executes a terminal command and returns its output.
    Args:
        command (str): The command to execute.
    Returns:
        str: The standard output and standard error of the command.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout + result.stderr
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}"

def read_from_memory(key: str) -> str:
    """
    Reads a value from the memory.
    Args:
        key (str): The key to read from the memory.
    Returns:
        str: The value from the memory.
    """
    return memory.get_from_short_term_memory(key) or memory.get_from_long_term_memory(key)

def write_to_memory(key: str, value: str):
    """
    Writes a value to the memory.
    Args:
        key (str): The key to write to the memory.
        value (str): The value to write to the memory.
    """
    memory.add_to_long_term_memory(key, value)
