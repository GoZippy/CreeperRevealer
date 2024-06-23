import cv2
import os
import yaml

# Load configuration
with open('../config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

input_dir = config['directories']['aligned']
output_dir = config['directories']['no_bg']
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)
    image = cv2.imread(filepath)
    if image is None:
        continue

    # Simplified background removal (for demo purposes)
    mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    output_filepath = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_nobg.png")
    cv2.imwrite(output_filepath, masked_image)
