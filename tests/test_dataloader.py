from src.datasets.dataloader import create_dataloader


loader = create_dataloader(
    "data/raw",
    batch_size=1
)


for batch in loader:
    print(batch.shape)
    break