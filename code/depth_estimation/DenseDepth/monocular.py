import PIL
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass, field
from keras.models import load_model
import pretrained_model


def stream_webcam(cap):
    ''' end video-stream by pressing Q '''
    while(True):
        ret, frame = cap.read()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def tf_inference(func, max_depth=1000, min_depth=10):
    ''' tf decorater func for Video class '''
    def func_wrapper(*args, **kwargs):
        frame = func(*args, **kwargs)

        if "model" in globals():
            frame_tf = frame[np.newaxis, ...]
            predictions = model.predict(frame_tf, batch_size=2)

            # needed? returns very small vals
            depth_frame = np.clip(predictions/max_depth, min_depth, max_depth) / max_depth

            return frame, predictions
        else:
            return frame

    return func_wrapper


@dataclass
class Video:
    '''
    Dataclass to manage video input with cv2

    src = 0 -> webcam
    '''
    src: int
    x_size: float
    y_size: float
    cap: object = field(init=False)

    def __post_init__(self):
        self.cap = cv2.VideoCapture(self.src)
        self.cap.set(3, self.x_size)
        self.cap.set(4, self.y_size)

    @tf_inference
    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame


if __name__ == "__main__":
    video = Video(cv2.CAP_DSHOW, 240, 320)

    # tf pretained model init:
    custom_objects = {'BilinearUpSampling2D': pretrained_model.BilinearUpSampling2D,
                      'depth_loss_function': None}
    model = load_model("pretrained_model/nyu.h5", custom_objects=custom_objects,
                        compile=False)

    while(True):
        frame = video.get_frame()

        if "model" in globals():
            # TODO: convert "raw" colormap to img
            depth_frame_raw = frame[1][0, :, :, :]
            depth_frame_raw *= 255.0 / depth_frame_raw.max()
            depth_frame_raw = np.array(depth_frame_raw, dtype=np.uint8)

            # colorize:
            depth_frame_color = cv2.applyColorMap(depth_frame_raw,
                                                  cv2.COLORMAP_PLASMA)

            #cv2.imshow("frame", frame[0])
            cv2.imshow("depth frame", depth_frame_color)
        else:
            cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
