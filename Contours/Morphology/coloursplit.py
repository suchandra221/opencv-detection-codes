import cv2

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

b, g, r = cv2.split(img)

cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.waitKey(0)
cv2.destroyAllWindows()