import cv2


def draw_grid(image, grid):

    output = image.copy()


    # Draw horizontal lines
    for line in grid.horizontal_lines:

        cv2.line(
            output,
            (line.x1, line.y),
            (line.x2, line.y),
            (0, 0, 255),
            2
        )


    # Draw vertical lines
    for line in grid.vertical_lines:

        cv2.line(
            output,
            (line.x, line.y1),
            (line.x, line.y2),
            (255, 0, 0),
            2
        )


    # Draw intersections
    for point in grid.intersections:

        cv2.circle(
            output,
            (point.x, point.y),
            3,
            (0, 255, 0),
            -1
        )


    # Draw cells
    for cell in grid.cells:

        x1, y1, x2, y2 = cell.bbox

        cv2.rectangle(
            output,
            (x1, y1),
            (x2, y2),
            (255, 255, 0),
            1
        )


    # Draw merged cells
    for merged in grid.merged_cells:

        x1, y1, x2, y2 = merged.bbox

        cv2.rectangle(
            output,
            (x1, y1),
            (x2, y2),
            (0, 255, 255),
            3
        )


    return output