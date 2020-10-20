import cv2
import numpy as np

#giving image path
img = cv2.imread("resources/3.jpg")

kernel = np.ones((5,5),np.uint8)

#GrayScale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur
imgBlur = cv2.GaussianBlur(img,(7,7),0)

imgCanny = cv2.Canny(img,100,100)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

#original Image
cv2.imshow("Original",img)

cv2.imshow("Grayscale",imgGray)

cv2.imshow("Blur",imgBlur)

cv2.imshow("Canny",imgCanny)

cv2.imshow("Dialation",imgDialation)

cv2.imshow("Eroded",imgEroded)
cv2.waitKey(0)