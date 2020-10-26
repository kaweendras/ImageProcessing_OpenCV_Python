import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img2 = np.zeros((512,512,3),np.uint8)
print(img,img2)


img[:] = 255,0,0 #blue color
img2[200:300,100:300] = 255,0,0 #blue color

cv2.imshow("image",img)
cv2.imshow("image only part",img2)

cv2.waitKey(0)