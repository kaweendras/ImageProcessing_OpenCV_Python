from turtle import width
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.circle(img , ( 300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText( img, 'hi im lakshan', (200, height - 10), font, 1.5 , (0,0,0), 5, cv2.LINE_AA)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()