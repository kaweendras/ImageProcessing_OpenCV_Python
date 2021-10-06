import cv2
import matplotlib.pyplot as plt

img = cv2.imread('resources/1.jpg')

channels = cv2.split(img)
colors = ('b','g','r')
plt.figure()
plt.title('Nivels of colors')
plt.xlabel('Intesity')
plt.ylabel('Count of pixels')
for (channel,color) in zip(channels,colors):
    hist = cv2.calcHist([channel],[0],None,[256],[0,256])
    plt.plot(hist,color=color)
    plt.xlim([0,256])
plt.show()