import imutils
from skimage import exposure
import numpy as np
import cv2

image = cv2.imread("raw_images/raw.png")
ratio = image.shape[0] / 300.0
orig = image.copy()

image = imutils.resize(image, height=600)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.bilateralFilter(gray, 11, 17, 17)
thresh = 255 - cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
edged = cv2.Canny(thresh, 20, 200)

cv2.imshow("", image)
cv2.waitKey(0)
cv2.destroyAllWindows()