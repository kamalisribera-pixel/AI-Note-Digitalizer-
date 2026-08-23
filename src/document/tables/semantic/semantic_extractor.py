from src.document.tables.semantic.row_detector import group_rows
from src.document.tables.semantic.column_detector import group_columns

from src.document.tables.cell import TableCell
from src.document.tables.table import Table


def extract_semantic_table(ocr_blocks):

    rows = group_rows(ocr_blocks)

    cells = []

    max_columns = 0

    for row_id, row in enumerate(rows):

        columns = group_columns(row["blocks"])

        max_columns = max(max_columns, len(columns))

        for column_id, column in enumerate(columns):

            block = column["blocks"][0]

            cell = TableCell(
                row_id=row_id,
                column_id=column_id,
                bbox=block["bbox"],
                text=block["text"],
                confidence=block.get("confidence", 1.0)
            )

            cells.append(cell)
    x1 = min(cell.bbox[0] for cell in cells)
    y1 = min(cell.bbox[1] for cell in cells)
    x2 = max(cell.bbox[2] for cell in cells)
    y2 = max(cell.bbox[3] for cell in cells)

    table_bbox = [x1, y1, x2, y2]

    table = Table(
        cells=cells,
        rows=len(rows),
        columns=max_columns,
        bbox=table_bbox,
        detection_method="semantic"
    )

    return table