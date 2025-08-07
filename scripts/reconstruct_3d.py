import argparse
import logging
import open3d as o3d
import os
import yaml


def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def main(config_path: str = 'config/config.yaml') -> None:
    logging.info("Loading configuration from %s", config_path)
    config = load_config(config_path)

    input_dir = config['directories']['depth_maps']
    output_dir = config['directories']['no_bg']
    os.makedirs(output_dir, exist_ok=True)

    logging.info("Starting 3D model reconstruction...")
    print("Starting 3D model reconstruction...")
    # TODO: Implement 3D reconstruction logic here using Open3D


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    parser = argparse.ArgumentParser(description='3D reconstruction from depth maps')
    parser.add_argument('--config', default='config/config.yaml', help='Path to YAML config file')
    args = parser.parse_args()
    main(args.config)
