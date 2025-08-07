import argparse
import logging
import torch
import cv2
import os
import yaml
from midas.model_loader import load_model


def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def main(config_path: str = 'config/config.yaml') -> None:
    logging.info("Loading configuration from %s", config_path)
    config = load_config(config_path)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model, transform = load_model(config['model_path'], device)

    input_dir = config['directories']['aligned']
    output_dir = config['directories']['depth_maps']
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        image = cv2.imread(filepath)
        if image is None:
            logging.warning("Unable to read image %s, skipping", filename)
            continue

        input_image = transform({"image": image})["image"]
        with torch.no_grad():
            prediction = model.forward(input_image.to(device)).cpu().numpy()

        depth_map = (255 * (prediction - prediction.min()) / (prediction.max() - prediction.min())).astype("uint8")
        output_filepath = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_depth.png")
        cv2.imwrite(output_filepath, depth_map)
        logging.info("Wrote %s", output_filepath)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    parser = argparse.ArgumentParser(description='Depth map generation (MiDaS)')
    parser.add_argument('--config', default='config/config.yaml', help='Path to YAML config file')
    args = parser.parse_args()
    main(args.config)
