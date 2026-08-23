from dataclasses import dataclass
from typing import List

from .cell import TableCell


@dataclass
class Table:
    cells: List[TableCell]

    rows: int
    columns: int

    bbox: List[int]

    detection_method: str = "unknown"