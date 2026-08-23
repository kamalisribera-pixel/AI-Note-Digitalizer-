def calculate_center_x(block):
    return (block["bbox"][0] + block["bbox"][2]) / 2


def group_columns(blocks, threshold=40):

    columns = []

    sorted_blocks = sorted(
        blocks,
        key=calculate_center_x
    )

    for block in sorted_blocks:

        x = calculate_center_x(block)

        placed = False

        for column in columns:

            if abs(x - column["center_x"]) <= threshold:
                column["blocks"].append(block)
                placed = True
                break

        if not placed:
            columns.append(
                {
                    "center_x": x,
                    "blocks": [block]
                }
            )

    return columns