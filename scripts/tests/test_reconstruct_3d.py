import os
import sys
import runpy
import types
import unittest
from unittest.mock import patch, mock_open


class TestReconstruct3DScript(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="directories:\n  depth_maps: data/depth_maps\n  no_bg: data/no_bg\n")
    @patch("os.makedirs")
    def test_reconstruct_placeholder(self, _makedirs, _open):
        yaml_module = types.SimpleNamespace(
            safe_load=lambda _f: {
                "directories": {"depth_maps": "data/depth_maps", "no_bg": "data/no_bg"}
            }
        )
        o3d_module = types.SimpleNamespace()
        with patch.dict("sys.modules", {"yaml": yaml_module, "open3d": o3d_module}):
            with patch.object(sys, 'argv', ['reconstruct_3d.py']):
                runpy.run_path(os.path.join(os.path.dirname(__file__), "..", "reconstruct_3d.py"), run_name="__main__")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)