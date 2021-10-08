import cv2
import numpy as np
import pandas as pd

main_img = cv2.imread("resources/4.jpg")

names = ['mean_r','mean_g','mean_b','stddev_r','stddev_g','stddev_b']
df = pd.DataFrame([], columns=names)

red_channel = main_img[:,:,0]
green_channel = main_img[:,:,1]
blue_channel = main_img[:,:,2]
blue_channel[blue_channel == 255] = 0
green_channel[green_channel == 255] = 0
red_channel[red_channel == 255] = 0

red_mean = np.mean(red_channel)
green_mean = np.mean(green_channel)
blue_mean = np.mean(blue_channel)

red_std = np.std(red_channel)
green_std = np.std(green_channel)
blue_std = np.std(blue_channel)

vector = [red_mean,green_mean,blue_mean,red_std,green_std,blue_std]

temp = pd.DataFrame([vector], columns=names)

print(temp)