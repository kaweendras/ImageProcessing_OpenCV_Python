import cv2

cap = cv2.VideoCapture("resources/video1.mp4")

#loop to show video Frame by Frame
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)

    # exitst when pressing q
    if cv2.waitKey(1)&0xFF ==ord('q'):
        break
