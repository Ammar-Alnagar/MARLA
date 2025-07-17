import argparse
from collaboration import Collaboration

def main():
    """
    Main function to run the agentic pipeline.
    """
    parser = argparse.ArgumentParser(description="Run the agentic pipeline.")
    parser.add_argument(
        "request",
        type=str,
        nargs="?",
        default="What is the weather in New York?",
        help="The request for the agents to process.",
    )
    args = parser.parse_args()

    # Create a collaboration object
    collaboration = Collaboration()

    # Run the pipeline
    collaboration.run_pipeline(args.request)

if __name__ == "__main__":
    main()
