import torch
import cv2
from model_loader import load_trt_model
from camera_utils import setup_camera
from inference_utils import preprocess_frame
from detection_logger import DetectionLogger


def run_inference(config):
    device = torch.device('cuda')
    model_trt = load_trt_model(config['tensorrt_model_path']).to(device)
    print("Model loaded successfully.")

    cap = setup_camera(config['webcam_index'])
    width, height = config['input_resolution']['width'], config['input_resolution']['height']
    logger = DetectionLogger()
    frame_count = 0
    start_time = cv2.getTickCount()
    inference_duration = config['inference_duration_seconds']

    print(f"Running inference for {inference_duration} seconds...")
    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < inference_duration:
        ret, frame = cap.read()
        if not ret:
            break

        img_tensor = preprocess_frame(frame, width, height, device)
        predictions = model_trt(img_tensor)

        # Log detections in memory
        logger.log_detection(frame_count, predictions.xyxy[0])

        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Write detections to file after all inferences are done
    logger.write_to_file(config['output_dir'])