import cv2
import base64
import numpy as np

image = cv2.imread("test.jpg")
outstr = base64.b64encode(image)

print(outstr)
#print(image.size, image.shape)