"""
Image Processing second course.

ROI - Region of Interest
- Selecting a part of an image for processing.
- From a point (x, y) to (x+w, y+h)
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    image = cv2.imread("./cat.png")
    x = 100
    y = 100
    w = 150
    h = 150

    # image_copy = image.copy()
    image[100: 150, 150: 200] = (255, 255, 0)

    roi = image[y: y + h, x: x + w]

    print(roi.shape)

    cv2.imshow("Image", image)
    cv2.imshow("ROI", roi)
    cv2.imshow("Image Copy", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
