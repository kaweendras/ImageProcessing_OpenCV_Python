import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img2 = np.zeros((512,512,3),np.uint8)

print(img)

cv2.rectangle(img,(10,10),(300,300),(0,55,0),3)
#^ (x,x),(x,x) -> starting poit and end point of the line ,(xxx,xxx,xxx)<- color ,X)<- thicckness

cv2.rectangle(img2,(10,10),(300,300),(0,55,0),cv2.FILLED)

cv2.imshow("image",img)
cv2.imshow("image-filled",img2)


cv2.waitKey(0)