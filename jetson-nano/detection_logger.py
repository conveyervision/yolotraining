import time


class DetectionLogger:
    def __init__(self):
        self.detections = []

    def log_detection(self, frame_number, detections):
        for detection in detections:
            x_center, y_center = self._get_center_coordinates(detection)
            self.detections.append((frame_number, len(detections), x_center, y_center))

    def _get_center_coordinates(self, detection):
        x1, y1, x2, y2 = detection[:4].int().tolist()
        x_center = (x1 + x2) // 2
        y_center = (y1 + y2) // 2
        return x_center, y_center

    def write_to_file(self, output_path):
        timestamp = int(time.time())
        filename = f"detections_{timestamp}.txt"
        with open(f"{output_path}/{filename}", "w") as file:
            for detection in self.detections:
                file.write(f"{detection}\n")
        print(f"Detections written to {output_path}/{filename}")