# YOLOv8 Inference with TensorRT on Jetson Nano

This project provides a way to run YOLOv8 object detection using TensorRT optimized models on an Nvidia Jetson Nano.

## Configuration

Before running the scripts, configure the `config.yaml` file to match your setup. Specify the paths to the original YOLOv8 PyTorch model and where you want to save the TensorRT model. Also, define the input resolution for both inference and the dummy input used during model conversion.

```yaml
# Example config.yaml
original_model_path: /path/to/original/yolov8_model.pt
tensorrt_model_path: /path/to/save/tensorrt_model.trt
input_resolution:
  width: 1280
  height: 720
webcam_index: 0
output_dir: output
conversion:
  dummy_input_resolution:
    width: 1280
    height: 720


Convert PyTorch Model to TensorRT

Run the following command to convert the PyTorch YOLOv8 model to a TensorRT model:

bash

python convertPTtoTensorRTModel.py

This will use the paths specified in the config.yaml file.
Run Inference

To perform inference with the webcam feed, simply run:

bash

python main.py

If you haven't converted the model yet, you can do so by running:

bash

python main.py -convertmodel

This will convert the model and then exit. After conversion, you can run the main.py script again to start the webcam feed and inference.

Press 'q' to quit the webcam feed.
Output

The processed frames with detected objects and bounding boxes will be saved in the directory specified by output_dir in the config.yaml file.