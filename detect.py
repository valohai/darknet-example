import os
import subprocess
from shutil import move

inputs_dir = os.getenv('VH_INPUTS_DIR', '/tmp/images')
outputs_dir = os.getenv('VH_OUTPUTS_DIR', '/tmp/predictions')

images_path = os.path.join(inputs_dir, 'images')
image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

# Darknet crashes if not in the directory: 'Couldn't open file: cfg/coco.data'
os.chdir('/darknet')

for image_filename in image_files:
    image_location = os.path.join(images_path, image_filename)
    error_code = subprocess.call([
        './darknet',
        'detect',
        './cfg/yolo.cfg',
        os.path.join(inputs_dir, 'yolo-weights/yolo.weights'),
        image_location,
    ])
    move('./predictions.jpg', os.path.join(outputs_dir, image_filename))
