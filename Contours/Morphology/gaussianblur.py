import cv2

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

blur = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()