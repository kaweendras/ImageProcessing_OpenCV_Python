import cv2

cap = cv2.VideoCapture(0)  #id of the web cam (0 = built in web cam-laptop)

#setting Resolution

cap.set(3,1366)
cap.set(4,768)

#Brightness cap.set(10,100)

#loop to show video Frame by Frame
while True:
    success, img = cap.read()
    cv2.imshow("Live Web cam feed",img)

    # exitst when pressing q
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break