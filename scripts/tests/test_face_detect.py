import os
import sys
import runpy
import types
import unittest
from unittest.mock import MagicMock, patch, mock_open


class TestFaceDetectScript(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="model_path: models/dummy.pt\ndirectories:\n  frames: data/frames\n  aligned: data/aligned\n")
    @patch("os.makedirs")
    @patch("os.listdir", return_value=["frame1.png"]) 
    def test_runs_and_writes_cropped_faces(self, _listdir, _makedirs, _open):
        # Fake image object supporting slicing image[y:y+h, x:x+w]
        class FakeImage:
            def __getitem__(self, key):
                return self

        # Fake cv2 with imread and imwrite
        fake_imwrite = MagicMock(return_value=True)
        cv2_module = types.SimpleNamespace(
            imread=lambda _path: FakeImage(),
            imwrite=fake_imwrite,
        )

        # Fake yaml with safe_load returning config
        yaml_module = types.SimpleNamespace(
            safe_load=lambda _f: {
                "model_path": "models/dummy.pt",
                "directories": {"frames": "data/frames", "aligned": "data/aligned"},
            }
        )

        # Fake dlib with a detector returning one rectangle
        dlib_module = types.ModuleType("dlib")

        class DummyRect:
            def left(self):
                return 10

            def top(self):
                return 20

            def width(self):
                return 30

            def height(self):
                return 40

        def get_frontal_face_detector():
            def detector(_img, _upsample):
                return [DummyRect()]

            return detector

        setattr(dlib_module, "get_frontal_face_detector", get_frontal_face_detector)

        with patch.dict("sys.modules", {"cv2": cv2_module, "yaml": yaml_module, "dlib": dlib_module}):
            with patch.object(sys, 'argv', ['face_detect.py']):
                runpy.run_path(os.path.join(os.path.dirname(__file__), "..", "face_detect.py"), run_name="__main__")

        # Ensure write was attempted with expected naming
        fake_imwrite.assert_called()
        args, _ = fake_imwrite.call_args
        self.assertIn(os.path.join("data", "aligned"), args[0])
        self.assertTrue(args[0].endswith("frame1_face_0.png"))


if __name__ == "__main__":
    unittest.main(verbosity=2)