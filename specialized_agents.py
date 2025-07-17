
from google.adk.agents import LlmAgent

file_agent = LlmAgent(
    name="FileAgent",
    model="gemini-2.0-flash",
    description="This agent is specialized in file operations like reading, writing, and searching for files.",
    instruction="You are a file management expert. You can read, write, and search for files on the local system.",
    # Tools for file operations will be added here later
    tools=[]
)

web_agent = LlmAgent(
    name="WebAgent",
    model="gemini-2.0-flash",
    description="This agent is specialized in web search and browsing.",
    instruction="You are a web expert. You can search the web and browse websites to find information.",
    # Tools for web operations will be added here later
    tools=[]
)




from tools import local_file_search, local_file_edit, web_search, terminal_use, read_from_memory, write_to_memory

file_agent.tools.extend([local_file_search, local_file_edit, read_from_memory, write_to_memory])
web_agent.tools.extend([web_search, read_from_memory, write_to_memory])

terminal_agent = LlmAgent(
    name="TerminalAgent",
    model="gemini-2.0-flash",
    description="This agent is specialized in executing terminal commands.",
    instruction="You are a terminal expert. You can execute commands in the terminal and return their output.",
    tools=[terminal_use, read_from_memory, write_to_memory]
)

