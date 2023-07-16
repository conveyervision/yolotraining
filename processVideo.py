# processVideo.py

import cv2
from ultralytics import YOLO

def process_video(video_path="output2.mp4"):
    # Load the YOLOv8 model
    model = YOLO('best.pt')

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Check if the user has pressed 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the video capture and close the window
    cap.release()
    cv2.destroyAllWindows()
