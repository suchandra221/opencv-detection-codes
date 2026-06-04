import cv2
import numpy as np

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(th, kernel, iterations=1)
dilation = cv2.dilate(th, kernel, iterations=1)
opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", img)
cv2.imshow("Threshold", th)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()