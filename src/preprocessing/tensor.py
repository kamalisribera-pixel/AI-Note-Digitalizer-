import numpy as np
import torch


def image_to_tensor(image: np.ndarray) -> torch.Tensor:
    tensor = torch.from_numpy(image)

    if tensor.ndim == 2:
        tensor = tensor.unsqueeze(0)
    else:
        tensor = tensor.permute(2, 0, 1)

    return tensor