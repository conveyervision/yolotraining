import cv2
import torch
import yaml
from torchvision.transforms import functional as F
from PIL import Image
import os
import sys
from torch2trt import TRTModule

def load_trt_model(trt_model_path):
    model_trt = TRTModule()
    model_trt.load_state_dict(torch.load(trt_model_path))
    return model_trt

def main(config):
    if "-convertmodel" in sys.argv:
        from convertPTtoTensorRTModel import convert_pt_to_trt
        convert_pt_to_trt(config['original_model_path'], config['tensorrt_model_path'])
        print("Conversion complete.")
        return

    if not os.path.exists(config['tensorrt_model_path']):
        print(f"TensorRT model not found at {config['tensorrt_model_path']}. Please run with '-convertmodel' to convert the PyTorch model first.")
        sys.exit(1)

    device = torch.device('cuda')
    model_trt = load_trt_model(config['tensorrt_model_path']).to(device)

    cap = cv2.VideoCapture(config['webcam_index'])
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    output_dir = config['output_dir']
    os.makedirs(output_dir, exist_ok=True)

    frame_count = 0
    width, height = config['input_resolution']['width'], config['input_resolution']['height']

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (width, height))
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        img_tensor = F.to_tensor(img).unsqueeze(0).to(device)

        predictions = model_trt(img_tensor)

        # Assuming predictions.xyxy[0] is a tensor with shape [N, 6] where N is the number of detections,
        # and each detection has (x1, y1, x2, y2, confidence, class_id)
        for detection in predictions.xyxy[0]:
            box = detection[:4].int().tolist()
            conf = detection[4].item()
            cls = detection[5].item()
            start = (box[0], box[1])
            end = (box[2], box[3])
            cv2.rectangle(frame, start, end, (0, 255, 0), 2)
            label = f"Class {int(cls)}: {conf:.2f}"
            cv2.putText(frame, label, (start[0], start[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imwrite(os.path.join(output_dir, f"frame_{frame_count}.jpg"), frame)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    main(config)