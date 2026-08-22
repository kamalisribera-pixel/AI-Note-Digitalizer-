import torch

from src.models.transformer_encoder import TransformerEncoder


model = TransformerEncoder()

tokens = torch.randn(
    1,
    49,
    768
)

output = model(tokens)

print(output.shape)