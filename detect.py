import subprocess
from shutil import move
from os import listdir
from os.path import isfile, join

images_path = '/tmp/images'
image_files = [f for f in listdir(images_path) if isfile(join(images_path, f))]

for image_filename in image_files:
    image_location = join(images_path, image_filename)
    error_code = subprocess.call([
        '/darknet/darknet',
        'detect',
        'cfg/yolo.cfg',
        '/tmp/yolo-weights/yolo.weights',
        image_location,
    ])
    move('/darknet/predictions.jpg', '/tmp/out/%s' % image_filename)
