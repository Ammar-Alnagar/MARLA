from agents import master_agent
from memory import Memory
from config import Config

class Collaboration:
    """
    Collaboration class for the multi-agent system.
    """
    def __init__(self):
        self.memory = Memory()

    def run_pipeline(self, request: str):
        """
        Runs the agentic pipeline for a given request.
        """
        print(f"Received request: {request}")

        # Add the request to the short-term memory
        self.memory.add_to_short_term_memory("request", request)

        # Main collaboration loop
        for i in range(Config.MAX_ITERATIONS):
            print(f"--- Iteration {i+1} ---")

            # Get the response from the master agent
            response = master_agent.run(request)

            # Add the response to the short-term memory
            self.memory.add_to_short_term_memory("response", response)

            print(f"Master Agent response: {response}")

            # Check if the task is complete
            if self._is_task_complete(response):
                print("Task completed successfully.")
                break

            # Update the request for the next iteration
            request = self._get_next_request(response)

        else:
            print("Max iterations reached. Task may not be complete.")

    def _is_task_complete(self, response: str) -> bool:
        """
        Checks if the task is complete based on the response.
        """
        return "task complete" in response.lower()

    def _get_next_request(self, response: str) -> str:
        """
        Generates the next request based on the previous response.
        """
        # For now, just return the response as the next request
        # In a real implementation, this would be more sophisticated
        return response
