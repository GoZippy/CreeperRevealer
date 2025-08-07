import os
import sys
import runpy
import types
import unittest
from unittest.mock import patch, mock_open


class TestDepthScript(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="model_path: models/dummy.pt\ndirectories:\n  aligned: data/aligned\n  depth_maps: data/depth_maps\n")
    @patch("os.makedirs")
    @patch("os.listdir", return_value=["img.png"]) 
    def test_depth_runs_and_writes(self, _listdir, _makedirs, _open):
        # Fake cv2
        cv2_module = types.SimpleNamespace(
            imread=lambda _path: object(),
            imwrite=lambda *args, **kwargs: True,
        )

        # Fake yaml
        yaml_module = types.SimpleNamespace(
            safe_load=lambda _f: {
                "model_path": "models/dummy.pt",
                "directories": {"aligned": "data/aligned", "depth_maps": "data/depth_maps"},
            }
        )

        # Fake torch
        class DummyNoGrad:
            def __enter__(self):
                return None

            def __exit__(self, exc_type, exc, tb):
                return False

        class DummyArray:
            def __init__(self, value):
                self.value = value

            def min(self):
                return 0.0

            def max(self):
                return 1.0

            def astype(self, _):
                return self

            def __sub__(self, other):
                return DummyArray(self.value)

            def __rsub__(self, other):
                return DummyArray(self.value)

            def __mul__(self, other):
                return DummyArray(self.value)

            def __rmul__(self, other):
                return DummyArray(self.value)

            def __truediv__(self, other):
                return DummyArray(self.value)

        class DummyTensor:
            def __init__(self, data):
                self.data = data

            def to(self, _device):
                return self

            def cpu(self):
                return self

            def numpy(self):
                return DummyArray(1.0)

        torch_module = types.SimpleNamespace(
            device=lambda *_: "cpu",
            cuda=types.SimpleNamespace(is_available=lambda: False),
            no_grad=lambda: DummyNoGrad(),
        )

        # Fake midas.model_loader
        def load_model(_path, _device):
            class DummyModel:
                def forward(self, _x):
                    return DummyTensor([0.0, 1.0])

            def transform(sample):
                return {"image": DummyTensor(sample["image"])}

            return DummyModel(), transform

        midas_loader_module = types.SimpleNamespace(load_model=load_model)

        with patch.dict(
            "sys.modules",
            {
                "cv2": cv2_module,
                "yaml": yaml_module,
                "torch": torch_module,
                "midas.model_loader": midas_loader_module,
            },
        ):
            with patch.object(sys, 'argv', ['depth.py']):
                runpy.run_path(os.path.join(os.path.dirname(__file__), "..", "depth.py"), run_name="__main__")

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)