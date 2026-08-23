from src.document.tables.semantic.column_detector import group_columns


row = [
    {
        "text": "Subject",
        "bbox": [100, 50, 200, 80]
    },
    {
        "text": "Marks",
        "bbox": [300, 50, 380, 80]
    },
    {
        "text": "Grade",
        "bbox": [500, 50, 600, 80]
    }
]


columns = group_columns(row)

for index, column in enumerate(columns):
    print(f"Column {index}")

    for block in column["blocks"]:
        print("  ", block["text"])

    print("-" * 20)