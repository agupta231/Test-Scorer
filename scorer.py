import numpy as np
import cv2
import glob


def determine_corner_type(x, y, image):
    buffer_size = 5




image_raw = cv2.imread("raw_images/raw.png")
gray = cv2.cvtColor(image_raw, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

corners = []

for y in reversed(xrange(len(thresh) / 2)):
    for x in xrange(len(thresh[0])):
        if thresh[x][y] == 255:
            determine_corner_type(x, y, thresh)

cv2.imshow("raw", image_raw)
cv2.imshow("thres_raw", thresh)

cv2.waitKey()
cv2.destroyAllWindows()

