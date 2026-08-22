import torch
from models.prototype.cnn import CNN
from src.datasets.dataloader import create_dataloader

model = CNN()

loader = create_dataloader("data/raw", batch_size=1)
images = next(iter(loader))
feature_maps = model.extract_features(images)
print("Feature maps shape:", feature_maps.shape)