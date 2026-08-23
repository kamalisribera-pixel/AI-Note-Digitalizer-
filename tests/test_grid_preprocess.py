import cv2

from src.document.tables.grid.preprocess import preprocess_table


image = cv2.imread("tests/images/grid/simple.png")

binary = preprocess_table(image)

cv2.imshow("Binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()