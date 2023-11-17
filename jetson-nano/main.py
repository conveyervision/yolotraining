import sys
from config_loader import load_config
from inference_runner import run_inference

def print_help_menu():
    help_menu = """
Usage: python main.py [OPTION]

Options:
  -convertmodel    Convert the PyTorch model to TensorRT and save it.
  -runinference    Run inference using the TensorRT model for the duration specified in config.yaml.

    """
    print(help_menu)

def main():
    config = load_config()

    if len(sys.argv) == 1:
        print_help_menu()
        return

    if "-convertmodel" in sys.argv:
        from convertPTtoTensorRTModel import convert_pt_to_trt
        convert_pt_to_trt(config['original_model_path'], config['tensorrt_model_path'])
        print("Conversion complete.")
        return

    if "-runinference" in sys.argv:
        run_inference(config)
        return

    print("Invalid option. Use -h for help.")
    print_help_menu()


if __name__ == "__main__":
    main()