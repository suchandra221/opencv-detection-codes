import cv2

img = cv2.imread("Images/crack.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

cv2.imshow("Cracks", edges)
cv2.waitKey(0)