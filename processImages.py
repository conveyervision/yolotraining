# processImages.py

import cv2
import os
import time
from ultralytics import YOLO

def process_images(images_directory="images", fps_limit=5):
    # Load the YOLOv8 model
    model = YOLO('best.pt')

    # Get a list of all files in the directory, sort them in ascending order
    image_files = sorted(os.listdir(images_directory), key=lambda x: int(x.split('_')[1].split('.')[0]))

    # Calculate delay for desired FPS
    delay = 1 / fps_limit

    # Loop through all the image files
    for image_file in image_files:
        start_time = time.time()

        # Read the image
        image_path = os.path.join(images_directory, image_file)
        image = cv2.imread(image_path)

        # Run YOLOv8 inference on the image
        results = model(image)

        # Visualize the results on the image
        annotated_image = results[0].plot()

        # Display the annotated image
        cv2.imshow("YOLOv8 Inference", annotated_image)

        # Check if the user has pressed 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Wait to maintain the desired FPS
        time_taken = time.time() - start_time
        if time_taken < delay:
            time.sleep(delay - time_taken)

    # Close the window
    cv2.destroyAllWindows()
