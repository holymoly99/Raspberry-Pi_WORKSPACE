# 연속 이미지 캡처
# 10초마다 계속 찍

from time import sleep
from picamera import PiCamera
camera = PiCamera()
camera.start_preview()
sleep(2)

# 파일명을 0부터
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(10) # wait 10 seconds

# # 파일명을 찍은 날짜로
# for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
#     print('Captured %s' % filename)
#     sleep(10)