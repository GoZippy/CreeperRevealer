import os
import runpy
import unittest
from unittest.mock import patch, MagicMock, mock_open


class TestBatchProcess(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="directories: {}\n")
    @patch("subprocess.run")
    def test_runs_scripts_in_order(self, mock_run, _open):
        # Simulate successful runs
        mock_proc = MagicMock()
        mock_proc.stdout = "OK"
        mock_proc.stderr = ""
        mock_proc.returncode = 0
        mock_run.return_value = mock_proc

        runpy.run_path(os.path.join(os.path.dirname(__file__), "..", "batch_process.py"), run_name="__main__")

        # Verify that subprocess.run was called for each script in order
        called_scripts = [call.args[0][1] for call in mock_run.call_args_list]
        expected = [
            "scripts/face_detect.py",
            "scripts/depth.py",
            "scripts/background_removal.py",
            "scripts/reconstruct_3d.py",
        ]
        self.assertEqual(called_scripts, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)