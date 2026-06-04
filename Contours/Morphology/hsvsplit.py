import cv2

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

cv2.imshow("Hue Channel", h)
cv2.imshow("Saturation Channel", s)
cv2.imshow("Value Channel", v)

cv2.waitKey(0)
cv2.destroyAllWindows()