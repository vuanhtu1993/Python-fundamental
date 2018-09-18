import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../image/galaxy.jpg', 0)
# px of image point coordinate
# px = img[100, 100]

# Accessing image properties
shape = img.shape
print(shape)
# Image ROI
# small_region = img[280:340, 330:390]
# img[273:333, 100:160] = small_region

# Split image channels
# b, g, r = cv2.split(img)
# print(b, g, r)

# Show image using cv2
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Show image using pyplot
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()
