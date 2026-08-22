import torch

from src.models.feature_adapter import FeatureAdapter


adapter = FeatureAdapter()

feature_maps = torch.randn(
    1,
    2048,
    7,
    7
)

tokens = adapter(feature_maps)

print(tokens.shape)