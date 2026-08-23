from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TableCell:
    row_id: int
    column_id: int

    bbox: List[int]

    text: str
    confidence: float = 1.0

    rowspan: int = 1
    colspan: int = 1

    style: Optional[dict] = None