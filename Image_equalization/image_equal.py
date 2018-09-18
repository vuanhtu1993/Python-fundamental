import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../image/pout.jpg', 0)  # The ',0' makes it read the image as a grayscale image
row, col = img.shape[:2]


# histogram function
# to make a histogram (count distribution frequency)
def df(img):
    values = [0] * 256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            values[int(img[i, j])] += 1
    return values


# cumulative distribution frequency
def cdf(hist):
    cdf = [0] * len(hist)  # len(hist) is 256
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i] = cdf[i - 1] + hist[i]
    # Now we normalize the histogram
    cdf = [ele * 255 / cdf[-1] for ele in cdf]  # What your function h was doing before
    return cdf


def equalize_image(image):
    my_cdf = cdf(df(img))
    # use linear interpolation of cdf to find new pixel values. Scipy alternative exists
    import numpy as np
    image_equalized = np.interp(image, range(0, 256), my_cdf)
    return image_equalized


image_eq = equalize_image(img)
hist_image = df(img)
hist_equalization = df(image_eq)
# create figure
plt.figure(1)
# create first subplot(numberRows, numberColumn, figureNumber)
plt.subplot(211)
plt.plot(hist_equalization, color='r')
# create second subplot(numberRows, numberColumn, figureNumber)
plt.subplot(212)
plt.plot(hist_image, color='b')
# Show figure
plt.show()
cv2.imwrite('equalized.png', image_eq)

