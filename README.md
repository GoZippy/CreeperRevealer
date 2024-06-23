# CreeperRevealer

CreeperRevealer is a tool designed to process video frames to detect, enhance, and reconstruct faces and human shapes in 3D. This project leverages various AI models to extract and enhance facial features, remove backgrounds, and perform 3D reconstruction from low-quality, low-resolution security footage.

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
CreeperRevealer/
├── config/
│   └── config.yaml
├── data/
│   ├── frames/
│   ├── aligned/
│   ├── depth_maps/
│   └── no_bg/
├── scripts/
│   ├── face_detect.py
│   ├── depth.py
│   ├── background_removal.py
│   └── reconstruct_3d.py
├── models/
│   └── dpt_beit_large_512.pt
├── LICENSE
├── README.md
└── requirements.txt
