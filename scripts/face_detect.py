import os
import cv2
import dlib
import yaml

# Load configuration
with open('../config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

detector = dlib.get_frontal_face_detector()

input_dir = config['directories']['frames']
output_dir = config['directories']['aligned']
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    filepath = os.path.join(input_dir, filename)
    image = cv2.imread(filepath)
    if image is None:
        continue

    faces = detector(image, 1)
    if len(faces) == 0:
        print(f"No faces detected in {filename}, skipping...")
        continue

    for i, face in enumerate(faces):
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cropped_face = image[y:y+h, x:x+w]
        output_filepath = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_face_{i}.png")
        cv2.imwrite(output_filepath, cropped_face)
