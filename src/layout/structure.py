from dataclasses import dataclass
from typing import List


@dataclass
class TextBlock:
    text: str
    bounding_box: List[int]
    confidence: float = 1.0

    block_type: str = "body"

    reading_order: int = 0
    alignment: str = "left"
    font_size: int = 0

    def to_dict(self):
        return {
            "text": self.text,
            "bounding_box": self.bounding_box,
            "confidence": self.confidence,
            "block_type": self.block_type,
            "reading_order": self.reading_order,
            "alignment": self.alignment,
            "font_size": self.font_size,
        }