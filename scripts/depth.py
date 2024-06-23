import torch
import cv2
import os
import yaml
from midas.model_loader import load_model

# Load configuration
with open('../config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, transform = load_model(config['model_path'], device)

input_dir = config['directories']['aligned']
output_dir = config['directories']['depth_maps']
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)
    image = cv2.imread(filepath)
    if image is None:
        continue

    input_image = transform({"image": image})["image"]
    with torch.no_grad():
        prediction = model.forward(input_image.to(device)).cpu().numpy()

    depth_map = (255 * (prediction - prediction.min()) / (prediction.max() - prediction.min())).astype("uint8")
    output_filepath = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_depth.png")
    cv2.imwrite(output_filepath, depth_map)
