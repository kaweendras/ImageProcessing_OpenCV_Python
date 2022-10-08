import cv2
import numpy as np

img = cv2.imread("1.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of red color in HSV
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)
red_only = cv2.bitwise_and(img,img, mask= mask)

#convert mask to 3-channel image to perform subtract
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

res = cv2.subtract(img,mask) #negative values become 0 -> black

cv2.imshow("img",img)
cv2.imshow("mask",mask)
cv2.imshow("red_only",red_only)
cv2.imshow("res",res)
cv2.waitKey()
cv2.destroyAllWindows()
