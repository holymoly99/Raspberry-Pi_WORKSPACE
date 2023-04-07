import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (640, 480)

    image = np.empty((480, 640, 3), dtype=np.uint8)

    # camera.capture로 소프트웨어적으로 컨트롤하기 떄무네 프레임이 낮다. 이를 위해 use_video_port=True 옵션을 준다
    while True:
        start = time.time()   # 반복문 시작 시간
        camera.capture(image, 'bgr', use_video_port=True)
        cv2.imshow('frame', image)
        
        if cv2.waitKey(1) == 27: # esc 키 입력시 종료
            break
        end = time.time() # 반복문 끝나는 시간
        fps = 1/(end-start) # 프레임 계산
        print(f'fps: {fps:0.1f}')