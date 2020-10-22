import subprocess
import cv2
import numpy as np
import base64

out = subprocess.run(["python","testpy2.py"], capture_output=True).stdout

manipulated = out[1:]
decout = base64.decodebytes(manipulated)

imgarr = np.frombuffer(decout, dtype=np.uint8)
image = np.reshape(imgarr, (1280, 890, 3)) # values from python2 image.shape

cv2.imshow("Python 3 image", image)
