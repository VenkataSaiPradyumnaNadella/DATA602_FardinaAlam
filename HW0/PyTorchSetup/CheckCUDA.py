## Name : Venkata Sai Pradyumna Nadella
## UID  : 122096059

import torch

print("Name : Venkata Sai Pradyumna Nadella\n", "UID  : 122096059")

if torch.cuda.is_available():
    print("PyTorch Version: ", torch.version)
    print("PyTorch Version: ", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("Number of GPUs:", torch.cuda.device_count())
    print("Current GPU:", torch.cuda.current_device())
    print("GPU Name:", torch.cuda.get_device_name(torch.cuda.current_device()))
else:
    print("No CUDA device available")