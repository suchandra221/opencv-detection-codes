import cv2
import numpy as np

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

if img is None:
    print("Image not found")
    exit()

img = cv2.resize(img, (600, 400))

blur = cv2.GaussianBlur(img, (7, 7), 0)

hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

mask = mask1 + mask2

kernel = np.ones((5, 5), np.uint8)

mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.dilate(mask, kernel, iterations=2)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

result = cv2.bitwise_and(img, img, mask=mask)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", blur)
cv2.imshow("HSV Image", hsv)
cv2.imshow("Threshold Mask", mask)
cv2.imshow("Final Extracted Color", result)

cv2.waitKey(0)
cv2.destroyAllWindows()