import cv2
from PIL import Image
from torchvision.transforms import functional as F

def preprocess_frame(frame, width, height, device):
    frame_resized = cv2.resize(frame, (width, height))
    img = Image.fromarray(cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB))
    img_tensor = F.to_tensor(img).unsqueeze(0).to(device)
    return img_tensor

def draw_predictions(frame, predictions):
    for detection in predictions.xyxy[0]:
        box = detection[:4].int().tolist()
        conf = detection[4].item()
        cls = detection[5].item()
        start = (box[0], box[1])
        end = (box[2], box[3])
        cv2.rectangle(frame, start, end, (0, 255, 0), 2)
        label = f"Class {int(cls)}: {conf:.2f}"
        cv2.putText(frame, label, (start[0], start[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame