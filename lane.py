import cv2

img = cv2.imread("Images/shapes.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150)

lines = cv2.HoughLinesP( edges, 1, 3.14/180, 100)

cv2.imshow("Lane", edges)
cv2.waitKey(0)