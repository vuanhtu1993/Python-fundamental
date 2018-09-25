import cv2
import pylab as plt
import matplotlib.image as mpimg
import numpy as np

# load image to numpy arrayb
# matplotlib 1.3.1 only supports png images
# use scipy or PIL for other formats
img = np.uint8(mpimg.imread('../image/home.png') * 255.0)
# img = cv2.imread('../image/caster.jpg', 0)
# convert to grayscale
# do for individual channels R, G, B, A for nongrayscale images

img = np.uint8((0.2126 * img[:, :, 0]) + np.uint8(0.7152 * img[:, :, 1]) + np.uint8(0.0722 * img[:, :, 2]))

# use hist module from hist.py to perform histogram equalization
from hist import histeq

new_img, h, new_h, sk = histeq(img)

# show old and new image
# show original image
plt.subplot(121)
plt.imshow(img)
plt.title('original image')
plt.set_cmap('gray')
# show original image
plt.subplot(122)
plt.imshow(new_img)
plt.title('hist. equalized image')
plt.set_cmap('gray')
plt.show()

# plot histograms and transfer function
fig = plt.figure()
fig.add_subplot(221)
plt.plot(h)
plt.title('Original histogram')  # original histogram

fig.add_subplot(222)
plt.plot(new_h)
plt.title('New histogram')  # hist of eqlauized image

fig.add_subplot(223)
plt.plot(sk)
plt.title('Transfer function')  # transfer function

plt.show()
