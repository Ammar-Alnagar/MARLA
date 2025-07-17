import json
import os
from collections import deque
from config import Config

class Memory:
    """
    Memory class for the multi-agent system.
    """
    def __init__(self):
        self.short_term_memory = deque(maxlen=Config.SHORT_TERM_MEMORY_SIZE)
        self.long_term_memory_file = Config.LONG_TERM_MEMORY_FILE
        self._load_long_term_memory()

    def _load_long_term_memory(self):
        """
        Loads the long-term memory from a JSON file.
        """
        if os.path.exists(self.long_term_memory_file):
            with open(self.long_term_memory_file, 'r') as f:
                self.long_term_memory = json.load(f)
        else:
            self.long_term_memory = {}

    def _save_long_term_memory(self):
        """
        Saves the long-term memory to a JSON file.
        """
        with open(self.long_term_memory_file, 'w') as f:
            json.dump(self.long_term_memory, f, indent=4)

    def add_to_short_term_memory(self, key: str, value: str):
        """
        Adds a key-value pair to the short-term memory.
        """
        self.short_term_memory.append({key: value})

    def get_from_short_term_memory(self, key: str) -> str:
        """
        Retrieves a value from the short-term memory based on the key.
        """
        for item in self.short_term_memory:
            if key in item:
                return item[key]
        return None

    def add_to_long_term_memory(self, key: str, value: str):
        """
        Adds a key-value pair to the long-term memory.
        """
        self.long_term_memory[key] = value
        self._save_long_term_memory()

    def get_from_long_term_memory(self, key: str) -> str:
        """
        Retrieves a value from the long-term memory based on the key.
        """
        return self.long_term_memory.get(key)
