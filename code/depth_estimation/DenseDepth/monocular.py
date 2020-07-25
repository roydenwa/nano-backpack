import PIL
import cv2
import tensorflow as tf
import numpy as np

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
    ''' tf decorater func for Video class'''
    def func_wrapper(*args, **kwargs):
        frame = func(*args, **kwargs)
        frame = frame[np.newaxis, ...]

        if model:
            predictions = model.predict(frame, batch_size=2)

        return np.clip(predictions/max_depth, min_depth, max_depth) / max_depth

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

    # tf model init:
    custom_objects = {'BilinearUpSampling2D': pretrained_model.BilinearUpSampling2D,
                      'depth_loss_function': None}
    model = load_model("pretrained_model/nyu.h5", custom_objects=custom_objects,
                        compile=False)

    while(True):
        frame = video.get_frame()
        print(frame.shape)

        # TODO: convert "raw" colormap to img
        '''
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    '''
