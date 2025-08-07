import os
import argparse
import logging
import cv2
import dlib
import yaml


def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def main(config_path: str = 'config/config.yaml') -> None:
    logging.info("Loading configuration from %s", config_path)
    config = load_config(config_path)

    detector = dlib.get_frontal_face_detector()

    input_dir = config['directories']['frames']
    output_dir = config['directories']['aligned']
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        image = cv2.imread(filepath)
        if image is None:
            logging.warning("Unable to read image %s, skipping", filename)
            continue

        faces = detector(image, 1)
        if len(faces) == 0:
            logging.info("No faces detected in %s, skipping", filename)
            continue

        for i, face in enumerate(faces):
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            cropped_face = image[y:y+h, x:x+w]
            output_filepath = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_face_{i}.png")
            cv2.imwrite(output_filepath, cropped_face)
            logging.info("Wrote %s", output_filepath)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    parser = argparse.ArgumentParser(description='Face detection and alignment')
    parser.add_argument('--config', default='config/config.yaml', help='Path to YAML config file')
    args = parser.parse_args()
    main(args.config)
