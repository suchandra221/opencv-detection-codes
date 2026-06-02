import cv2

img = cv2.imread("Images/shapes.jpg", 0)

edges = cv2.Canny(img, 30, 100)

cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()