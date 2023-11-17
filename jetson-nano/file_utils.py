import os
import cv2

def save_frame(output_dir, frame, frame_count):
    os.makedirs(output_dir, exist_ok=True)
    cv2.imwrite(os.path.join(output_dir, f"frame_{frame_count}.jpg"), frame)