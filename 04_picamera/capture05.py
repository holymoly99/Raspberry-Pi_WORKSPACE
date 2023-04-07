# 캡처 이미지 크기조정

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

# 카메라 웜업
sleep(2)

camera.capture('foo.jpg', resize=(320, 240))