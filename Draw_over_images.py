import cv2
import numpy as np
# Create a black image
image = np.zeros((512,512,3), np.uint8)
# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)
cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Black Rectangle (B&W)", image_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
