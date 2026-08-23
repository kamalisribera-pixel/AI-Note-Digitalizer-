from src.document.tables.semantic.semantic_extractor import extract_semantic_table


ocr_blocks = [
    {
        "text": "Subject",
        "bbox": [100, 50, 200, 80]
    },
    {
        "text": "Marks",
        "bbox": [300, 50, 380, 80]
    },
    {
        "text": "Math",
        "bbox": [100, 100, 180, 130]
    },
    {
        "text": "95",
        "bbox": [300, 100, 330, 130]
    },
    {
        "text": "Physics",
        "bbox": [100, 150, 200, 180]
    },
    {
        "text": "90",
        "bbox": [300, 150, 330, 180]
    }
]

table = extract_semantic_table(ocr_blocks)

print("Rows:", table.rows)
print("Columns:", table.columns)
print("Table BBox:", table.bbox)
print()

for cell in table.cells:
    print(
        f"Row {cell.row_id}, "
        f"Column {cell.column_id} -> "
        f"{cell.text}"
    )