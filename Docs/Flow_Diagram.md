```mermaid
flowchart LR
    A[Input video frames\n`data/frames`] --> B[Face detection & alignment\n`scripts/face_detect.py`\n-> `data/aligned`]
    B --> C[Depth estimation (MiDaS)\n`scripts/depth.py`\n-> `data/depth_maps`]
    C --> D[Background removal\n`scripts/background_removal.py`\n-> `data/no_bg`]
    D --> E[3D reconstruction (TBD)\n`scripts/reconstruct_3d.py`\n-> output models]

    subgraph Config
    F[`config/config.yaml`]
    end
    F -. directories/model_path .-> B
    F -. directories/model_path .-> C
    F -. directories .-> D
    F -. directories .-> E
```