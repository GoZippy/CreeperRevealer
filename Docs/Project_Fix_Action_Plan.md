### Project Fix Action Plan

- **Path handling**
  - Refactor scripts to accept `--config` path and resolve relative to repo root; avoid `../config/config.yaml`.
  - Use `pathlib.Path` and robust existence checks.

- **Modularization**
  - Move procedural code into callable functions (e.g., `detect_faces`, `estimate_depth`, `remove_background`, `reconstruct_mesh`).
  - Add `if __name__ == "__main__":` entrypoints with `argparse`.

- **Dependencies and models**
  - Add `midas` loader dependency or vendor minimal loader; provide model download script with checksum.
  - Provide CPU fallback and configurable device selection.

- **Error handling & logging**
  - Implement structured logging; surface warnings for skipped files; fail-fast options.

- **Testing**
  - Keep unit tests with mocks; add integration tests with small sample images committed via git-lfs.
  - Set up CI (GitHub Actions) for CPU-only test matrix.

- **3D reconstruction**
  - Implement actual pipeline (e.g., Poisson/screened Poisson, TSDF, or depth-to-point-cloud + meshing) and persist `.ply`/`.obj` outputs.

- **Documentation**
  - Fix README typos/steps; document full pipeline, CLI usage, and environment setup.

- **Packaging**
  - Provide a `setup.py` or `pyproject.toml`; optional CLI entry point `creeperrevealer`.