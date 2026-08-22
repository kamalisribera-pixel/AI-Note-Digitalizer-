from pathlib import Path

import cv2

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

NOTES_DIR = DATA_DIR / "raw"

OUTPUT_DIR = PROJECT_ROOT / "OUTPUTS"

IMAGE_SIZE=(224,224)

SUPPORTED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp",
)

# Denoising
MEDIAN_KERNEL_SIZE = 3
#Contrast Enhancement
CLAHE_CLIP_LIMIT = 2.0
CLAHE_TILE_GRID_SIZE = (8, 8)

# Threshold
THRESHOLD_MIN_VALUE = 0
THRESHOLD_MAX_VALUE = 255
THRESHOLD_ADAPTIVE_METHOD = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
THRESHOLD_TYPE = cv2.THRESH_BINARY
THRESHOLD_BLOCK_SIZE = 11
THRESHOLD_C = 2
