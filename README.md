# CreeperRevealer

CreeperRevealer is a tool designed to process video frames to detect, enhance, and reconstruct faces and human shapes in 3D. This project leverages various AI models to extract and enhance facial features, remove backgrounds, and perform 3D reconstruction from low-quality, low-resolution security footage.

CreeperRevealer is an advanced Python-based toolkit designed for forensic analysis of video footage. Leveraging state-of-the-art AI models, CreeperRevealer processes video frames to detect and reconstruct obscured faces and generate detailed 3D models of suspects. This project integrates facial recognition, depth estimation, and 3D reconstruction to aid law enforcement in identifying and capturing perpetrators from low-quality security footage.

## Features

- Face detection and alignment
- Depth map generation using MiDaS
- Background removal
- 3D model reconstruction

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GoZippy/CreeperRevealer.git
   cd CreeperRevealer

## Directory Structure
```plaintext
CreeperRevealer/
├── config/
│   └── config.yaml
├── data/
│   ├── frames/
│   ├── aligned/
│   ├── depth_maps/
│   └── no_bg/
├── scripts/
│   ├── batch_process.py
│   ├── face_detect.py
│   ├── depth.py
│   ├── background_removal.py
│   └── reconstruct_3d.py
├── models/
│   └── dpt_beit_large_512.pt
├── LICENSE
├── README.md
├── requirements.txt
└── environment.yaml
```

2. Install the required packages:
```bash
conda env create -f environment.yaml
conda activate creeperrevealer
```
3. Place your video frames in the data/frames directory.

## Usage

1. Run face detection
```bash
python scripts/face_detect.py
```
2. Generate depth maps:
```bash
python scripts/background_removal.py
```
3. Remove backgrounds
```bash
python scripts/background_removal.py
```
4. Perform 3D reconstruction:
```bash
python scripts/reconstruct_3d.py
```

## Law Enforcement and Commercial Use please contact us for license.


