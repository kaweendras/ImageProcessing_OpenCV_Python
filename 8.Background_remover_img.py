import cv2
import numpy as np

main_img = cv2.imread("resources/4.jpg")

img = cv2.cvtColor(main_img, cv2.COLOR_BGR2RGB)
resized_image = cv2.resize(img, (1400, 1000))
size_y,size_x,_ = img.shape
gr_scale = cv2.cvtColor(resized_image,cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gr_scale, (5,5),0)
ret_otsu,im_bw_otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((50,50),np.uint8)
closing = cv2.morphologyEx(im_bw_otsu, cv2.MORPH_CLOSE, kernel)
    
contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
contains = []
y_ri,x_ri, _ = resized_image.shape
for cc in contours:
    yn = cv2.pointPolygonTest(cc,(x_ri//2,y_ri//2),False)
    contains.append(yn)

val = [contains.index(temp) for temp in contains if temp>0]
index = val[0]
    
black_img = np.empty([1000,1400,3],dtype=np.uint8)
black_img.fill(0)
    
cnt = contours[index]
mask = cv2.drawContours(black_img, [cnt] , 0, (255,255,255), -1)
    
maskedImg = cv2.bitwise_and(resized_image, mask)
white_pix = [255,255,255]
black_pix = [0,0,0]
    
final_img = maskedImg
h,w,channels = final_img.shape
for x in range(0,w):
    for y in range(0,h):
        channels_xy = final_img[y,x]
        if all(channels_xy == black_pix):
            final_img[y,x] = white_pix


cv2.imshow("output",final_img)

cv2.waitKey(0)