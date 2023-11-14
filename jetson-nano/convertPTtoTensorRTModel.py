import torch
import yaml
from torch2trt import torch2trt
from models.experimental import attempt_load  # Assuming this is the correct import for YOLOv8

def convert_pt_to_trt(model_path, trt_model_path):
    device = torch.device('cuda')
    model = attempt_load(model_path, map_location=device)
    model.eval()

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    width = config['conversion']['dummy_input_resolution']['width']
    height = config['conversion']['dummy_input_resolution']['height']
    dummy_input = torch.ones((1, 3, height, width)).to(device)

    # Convert the model using torch2trt
    model_trt = torch2trt(model, [dummy_input], fp16_mode=True)  # Enable fp16_mode if supported

    # Save the converted model
    torch.save(model_trt.state_dict(), trt_model_path)
    print(f"Model successfully converted to TensorRT and saved at {trt_model_path}")


if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    convert_pt_to_trt(config['original_model_path'], config['tensorrt_model_path'])