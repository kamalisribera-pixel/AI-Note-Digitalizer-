from torch.utils.data import DataLoader
from src.datasets.dataset import NoteDataset

def create_dataloader(
    image_directory, 
    batch_size=32, 
    shuffle=True, 
    num_workers=4
):
    dataset = NoteDataset(image_directory)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    return dataloader