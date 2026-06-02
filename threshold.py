import cv2

img = cv2.imread("Images/shapes.jpg", 0)

_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

print(thresh)