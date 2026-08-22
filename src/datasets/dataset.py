from pathlib import Path
from torch.utils.data import Dataset
from src.preprocessing.pipline import PreprocessingPipeline

class NoteDataset(Dataset):
    def __init__(self, image_directory):
        self.image_directory = Path(image_directory)
        self.image_paths = sorted(self.image_directory.glob("*"))
        self.pipeline = PreprocessingPipeline()

    def __len__(self):
        return len(self.image_paths)
    def __getitem__(self, idx):
        image_path = str(self.image_paths[idx])
        processed_image = self.pipeline.process(image_path)
        return processed_image