import os

class Config:
    """
    Configuration class for the multi-agent system.
    """
    # Path to the long-term memory file
    LONG_TERM_MEMORY_FILE = os.path.join("memory", "long_term_memory.json")

    # Short-term memory size
    SHORT_TERM_MEMORY_SIZE = 5

    # Maximum number of iterations for the collaboration loop
    MAX_ITERATIONS = 10
