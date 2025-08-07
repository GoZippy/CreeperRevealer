import argparse
import logging
import cv2
import os
import yaml


def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def main(config_path: str = 'config/config.yaml') -> None:
    logging.info("Loading configuration from %s", config_path)
    config = load_config(config_path)

    input_dir = config['directories']['aligned']
    output_dir = config['directories']['no_bg']
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        image = cv2.imread(filepath)
        if image is None:
            logging.warning("Unable to read image %s, skipping", filename)
            continue

        mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
        masked_image = cv2.bitwise_and(image, image, mask=mask)

        output_filepath = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_nobg.png")
        cv2.imwrite(output_filepath, masked_image)
        logging.info("Wrote %s", output_filepath)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    parser = argparse.ArgumentParser(description='Background removal')
    parser.add_argument('--config', default='config/config.yaml', help='Path to YAML config file')
    args = parser.parse_args()
    main(args.config)
