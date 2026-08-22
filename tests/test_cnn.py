import torch

from models.prototype.cnn import CNN


model = CNN()

image = torch.randn(
    1,
    1,
    224,
    224
)

output = model(image)

print(output.shape)