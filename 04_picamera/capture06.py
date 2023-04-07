from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate=30)
camera.iso = 100
sleep(2)
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
# 고정된 설정으로 여러 사진 찍기
# 파이썬 []은 "컴프리텐션"이라 불리며 해당 반복문으로 리스트를 만들어라
camera.capture_sequence([f'image{i:02d}.jpg' for i in range(10)])