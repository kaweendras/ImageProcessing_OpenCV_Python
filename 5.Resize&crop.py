import cv2
import numpy as np

img =cv2.imread("resources/2.jpg")

#getting the size of the image (height X width X channel)
print(img.shape)

imgResize =cv2.resize(img,(300,200)) #resizing w x h

imgCropped = img[0:200,200:500] #h x w

cv2.imshow("Image",img) #original

cv2.imshow("ReSize",imgResize) #resized

cv2.imshow("Cropped",imgCropped) #cropped

cv2.waitKey(0)