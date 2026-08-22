from PIL import Image
from src.ocr.cropper import ImageCropper


image = Image.open(
    "data/raw/notes.png"
)

cropper = ImageCropper()

crop = cropper.crop(
    image,
    [227, 0, 598, 34],
    padding=20
)

crop.save(
    "data/raw/test_crop.png"
)

print("Crop saved")