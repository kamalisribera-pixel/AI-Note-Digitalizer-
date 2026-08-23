from src.document.tables.cell import TableCell
from src.document.tables.table import Table


cell = TableCell(
    row_id=0,
    column_id=0,
    bbox=[100, 100, 200, 130],
    text="Subject",
    confidence=0.98
)


table = Table(
    cells=[cell],
    rows=1,
    columns=1,
    bbox=[100, 100, 200, 130],
    detection_method="semantic"
)


print(table)
print(table.cells[0])