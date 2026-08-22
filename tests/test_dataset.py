from src.datasets.dataset import NoteDataset

dataset = NoteDataset("data/raw")
print(len(dataset))
image = dataset[0]
print(image.shape)