import os
from calculatecenterline import compute_center_y
from cropimgs import crop_image
from adjustboundarybox import adjust_bounding_boxes

def process_files(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.txt'):
            image_file = file.replace('.txt', '.jpg')
            center_y = compute_center_y(os.path.join(directory, file))
            crop_image(os.path.join(directory, image_file), center_y)
            adjust_bounding_boxes(os.path.join(directory, file), center_y)

process_files('/Users/saadm/PycharmProjects/yolotraining/preprocessing/labelImg')
