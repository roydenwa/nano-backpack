import PIL
import cv2
import tensorflow as tf

from dataclasses import dataclass, field


def stream_webcam(cap):
    ''' end video-stream by pressing Q '''
    while(True):
        ret, frame = cap.read()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


@dataclass
class Video:
    '''
    Dataclass to manage video input with cv2

    src = 0 -> webcam
    '''
    src: int
    cap: object = field(init=False)

    def __post_init__(self):
        self.cap = cv2.VideoCapture(self.src)

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame


if __name__ == "__main__":
    video = Video(cv2.CAP_DSHOW)

    while(True):
        frame = video.get_frame()
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
