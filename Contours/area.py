import cv2

img = cv2.imread(r"C:\Personal\opencv practice\Images\shapes.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours( thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        

    for c in contours:
        area = cv2.contourArea(c)

        if area > 500:
            cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
            print("Contour Area:", area)

    cv2.imshow("Filtered Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()