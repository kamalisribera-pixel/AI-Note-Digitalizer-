from .table_block import TableBlock

class TableBuilder:

    def build(self, cells, bbox):

        if not cells:
            return None

        max_row = max(
            cell.row_id
            for cell in cells
        )

        max_col = max(
            cell.column_id
            for cell in cells
        )

        table = [
            ["" for _ in range(max_col + 1)]
            for _ in range(max_row + 1)
        ]

        for cell in cells:

            table[cell.row_id][cell.column_id] = cell.text

        return TableBlock(
            rows=table,
            bbox=bbox,
            confidence=1.0
        )