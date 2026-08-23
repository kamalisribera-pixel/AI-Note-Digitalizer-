from dataclasses import dataclass
from typing import Optional


@dataclass
class ImageBlock:

    bbox: tuple

    image_type: str = "unknown"

    confidence: float = 1.0

    caption: Optional[str] = None

    metadata: Optional[dict] = None