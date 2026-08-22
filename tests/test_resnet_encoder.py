from src.models.resnet_encoder import ResNetEncoder

import torch


model = ResNetEncoder()

images = torch.randn(1, 3, 224, 224)  # Example input tensor
feature_maps = model(images)
print("Feature maps shape:", feature_maps.shape)