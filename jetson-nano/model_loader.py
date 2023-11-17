import torch
from torch2trt import TRTModule

def load_trt_model(trt_model_path):
    model_trt = TRTModule()
    model_trt.load_state_dict(torch.load(trt_model_path))
    return model_trt