import cv2

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:
        area = cv2.contourArea(c)

        if area > 500:
            perimeter = cv2.arcLength(c, True)

            approx = cv2.approxPolyDP(c, 0.02*perimeter , True)
        
            edges = len(approx)

            if edges == 3:
                shape = "Triangle"
            elif edges == 4:
                shape = "Rectangle/Square"
            elif edges == 5:
                shape = "Pentagon"
            elif edges == 6:
                shape = "Hexagon"
            elif edges > 8:
                shape = "Circle"
            else:
                shape = "Random Shape"

            x, y, w, h = cv2.boundingRect(approx)

            cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
            cv2.putText(img, shape, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            print(shape, "Edges:", edges, "Area:", area)

    cv2.imshow("Shape Classification", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()