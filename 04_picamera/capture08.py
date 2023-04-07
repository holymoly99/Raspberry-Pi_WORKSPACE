# numpy 배열에 저장해서 OpenCV에 적용하기
# OpenCV 객체로 캡처
import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (640, 480)

    image = np.empty((480, 640, 3), dtype=np.uint8)  # 높은 차원인 높이(480)부터 나오는 것에 주의!
    camera.capture(image, 'bgr')
    cv2.imshow('frame', image)
    cv2.waitKey(0)