import numpy as np
import glob
import cv2
import imutils

template = cv2.imread("pattern.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
tH, tW = template.shape[:2]

image = cv2.imread("raw_images/raw.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
found = None

for scale in np.linspace(0.2, 1, 20)[::-1]:
    resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
    r = gray.shape[1] / float(resized.shape[1])

    if resized.shape[0] < tH or resized.shape[1] < tW:
        break

    edged = 255 - cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    clone = np.dstack([edged, edged, edged])
    cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                  (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
    cv2.imshow("Visualize", clone)
    cv2.waitKey(0)


cv2.imshow("s", template)

cv2.waitKey(0)
cv2.destroyAllWindows()