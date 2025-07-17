import unittest
from unittest.mock import patch, MagicMock
from collaboration import Collaboration

class TestCollaboration(unittest.TestCase):
    """
    Unit tests for the Collaboration class.
    """

    @patch('collaboration.master_agent')
    def test_run_pipeline(self, mock_master_agent):
        """
        Tests the run_pipeline method of the Collaboration class.
        """
        # Mock the master agent's run method
        mock_master_agent.run.return_value = "Task complete."

        # Create a collaboration object
        collaboration = Collaboration()

        # Run the pipeline
        collaboration.run_pipeline("Test request")

        # Assert that the master agent's run method was called
        mock_master_agent.run.assert_called_once_with("Test request")

if __name__ == '__main__':
    unittest.main()
