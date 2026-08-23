from dataclasses import dataclass
from typing import List


@dataclass
class DocumentBlock:
    text: str
    bbox: List[int]
    confidence: float = 1.0

    # Classification
    block_type: str = "unknown"
    heading_level: int = 0

    # Geometry features
    width: int = 0
    height: int = 0
    width_ratio: float = 0.0

    # Text features
    word_count: int = 0
    char_count: int = 0
    uppercase_ratio: float = 0.0
    has_numbering: bool = False
    numbering_type: str = ""

    # Layout features
    gap_above: int = 0
    gap_below: int = 0
    center_offset: float = 0.0

    # Reading structure
    reading_order: int = 0
    alignment: str = "left"


    def to_dict(self):
        return {
            "text": self.text,
            "bbox": self.bbox,
            "confidence": self.confidence,
            "block_type": self.block_type,
            "heading_level": self.heading_level,
            "width": self.width,
            "height": self.height,
            "word_count": self.word_count,
            "char_count": self.char_count,
            "uppercase_ratio": self.uppercase_ratio,
            "gap_above": self.gap_above,
            "gap_below": self.gap_below,
            "center_offset": self.center_offset,
            "reading_order": self.reading_order,
            "alignment": self.alignment,
            "has_numbering": self.has_numbering,
            "numbering_type": self.numbering_type,
        }