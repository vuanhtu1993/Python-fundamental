import cv2
import logging
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image/bakc.jpg', 0)
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    logging.info(i)
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(histr, color=col)
    # plt.xlim([0, 256])
plt.show()
