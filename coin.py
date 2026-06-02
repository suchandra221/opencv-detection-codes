
import cv2

img = cv2.imread("Images/coin.png",0)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=100, param2=30, minRadius=10, maxRadius=100)
print("Coins:", len(circles[0]))