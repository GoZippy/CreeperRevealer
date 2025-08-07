### Enhancements and UX/UI Improvements

- **CLI UX**
  - Progress bars, verbose/debug flags, dry-run mode, and colored logs.
  - Fail/skip policies; resumable processing; per-step enable/disable.

- **Visualization**
  - Generate HTML report with before/after images, depth maps, and 3D preview (e.g., using Open3D screenshot or Plotly).

- **Config management**
  - Support `.env`, YAML schema validation, and per-run overrides.

- **Web UI (optional)**
  - Lightweight dashboard via Streamlit or FastAPI + React to upload frames, view outputs, and download models.

- **Performance**
  - Batch inference, mixed precision when supported, and caching of intermediate results.

- **Quality**
  - Face alignment improvements (landmarks), better background matting (e.g., MODNet or Robust Video Matting).

- **DevEx**
  - Pre-commit hooks for formatting/linting; type hints; clearer README with examples.