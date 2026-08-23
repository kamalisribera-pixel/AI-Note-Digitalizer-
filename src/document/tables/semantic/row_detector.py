def calculate_center_y(block):
    return (block["bbox"][1] + block["bbox"][3]) / 2


def group_rows(blocks, threshold=20):

    rows = []

    sorted_blocks = sorted(
        blocks,
        key=calculate_center_y
    )

    for block in sorted_blocks:

        y = calculate_center_y(block)

        placed = False

        for row in rows:
            row_y = row["center_y"]

            if abs(y - row_y) <= threshold:
                row["blocks"].append(block)
                placed = True
                break

        if not placed:
            rows.append(
                {
                    "center_y": y,
                    "blocks": [block]
                }
            )

    return rows