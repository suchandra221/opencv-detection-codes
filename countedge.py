import cv2

img = cv2.imread("Images/shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 500:
        perimeter = cv2.arcLength(c, True)

        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

        edges = len(approx)

        if edges == 3:
            shape = "Triangle"
        elif edges == 4:
            shape = "Rectangle/Square"
        elif edges > 8:
            shape = "Circle"
        else:
            shape = "Random Shape"

        print(shape, "Edges/Corners:", edges)

        cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)

cv2.imshow("Detected Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()