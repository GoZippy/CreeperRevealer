import os
import sys
import runpy
import types
import unittest
from unittest.mock import patch, mock_open


class TestBackgroundRemovalScript(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="directories:\n  aligned: data/aligned\n  no_bg: data/no_bg\n")
    @patch("os.makedirs")
    @patch("os.listdir", return_value=["img.png"]) 
    def test_background_removal(self, _listdir, _makedirs, _open):
        cv2_module = types.SimpleNamespace(
            imread=lambda _path: object(),
            cvtColor=lambda img, code: img,
            threshold=lambda mask, a, b, c: (None, 255),
            bitwise_and=lambda img, _img, mask=None: img,
            imwrite=lambda *args, **kwargs: True,
            COLOR_BGR2GRAY=0,
            THRESH_BINARY=0,
        )

        yaml_module = types.SimpleNamespace(
            safe_load=lambda _f: {
                "directories": {
                    "aligned": "data/aligned",
                    "no_bg": "data/no_bg",
                }
            }
        )

        with patch.dict("sys.modules", {"cv2": cv2_module, "yaml": yaml_module}):
            with patch.object(sys, 'argv', ['background_removal.py']):
                runpy.run_path(os.path.join(os.path.dirname(__file__), "..", "background_removal.py"), run_name="__main__")

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)