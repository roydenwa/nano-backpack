import PIL
import cv2
import tensorflow as tf


def stream_webcam(cap):
    while(True):
        ret, frame = cap.read()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)
    stream_webcam(cap)
