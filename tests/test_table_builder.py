from src.document.tables.table_builder import TableBuilder
from src.document.tables.cell import TableCell


cells = [
    TableCell(
        row_id=0,
        column_id=0,
        bbox=[0,0,50,20],
        text="Name"
    ),

    TableCell(
        row_id=0,
        column_id=1,
        bbox=[50,0,100,20],
        text="Age"
    ),

    TableCell(
        row_id=1,
        column_id=0,
        bbox=[0,20,50,40],
        text="Raj"
    ),

    TableCell(
        row_id=1,
        column_id=1,
        bbox=[50,20,100,40],
        text="18"
    )
]


builder = TableBuilder()

table = builder.build(
    cells,
    bbox=(0,0,100,40)
)


print("TABLE RESULT")
print(table.rows)
print(table)