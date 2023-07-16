# imagestomp4.py

import cv2
import os
import re

def convert_images_to_mp4(image_folder='testing_images', video_name='output.mp4', fps=5):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

    # Function to extract numbers from the image filename
    def extract_number(img_name):
        return int(re.search(r'\d+', img_name).group())

    # Sort the images by the number in their filename
    images.sort(key=extract_number)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec using VideoWriter_fourcc and create a VideoWriter object
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Write each image to the video file
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Close the video file
    video.release()
