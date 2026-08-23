from src.document.tables.semantic.row_detector import group_rows


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


rows = group_rows(ocr_blocks)

for index, row in enumerate(rows):
    print(f"Row {index}")

    for block in row["blocks"]:
        print("  ", block["text"])

    print("-" * 20)