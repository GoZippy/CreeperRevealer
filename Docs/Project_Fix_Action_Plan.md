### Project Fix Action Plan

- **Path handling**
  - DONE: Scripts accept `--config` and default to `config/config.yaml`.
  - NEXT: Centralize path resolution with `pathlib.Path` and ensure output directories are created lazily.

- **Modularization**
  - DONE: Converted scripts to `main()` with argparse and structured logging.
  - NEXT: Extract core logic into reusable functions and a small library module (e.g., `crlib/processing.py`).

- **Dependencies and models**
  - NEXT: Add model download helper with checksum; document CPU/GPU selection flag and environment variable.

- **Error handling & logging**
  - DONE: Basic logging added.
  - NEXT: Structured logging, file logging option, and better exception surfacing.

- **Testing**
  - DONE: Unit tests for each script including orchestrator.
  - NEXT: Add small integration tests with sample images (if licensing permits) and extend CI.

- **3D reconstruction**
  - NEXT: Implement depth-to-point-cloud and meshing pipeline with `.ply` output; add unit/integration tests.

- **Documentation**
  - NEXT: Update README with new CLI usage; add examples.

- **Packaging**
  - NEXT: `pyproject.toml` and CLI entry-point.