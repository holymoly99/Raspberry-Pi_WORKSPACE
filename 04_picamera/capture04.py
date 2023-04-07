# PIL 객체로 캡처

from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image
# Create the in-memory stream
stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')
# 내용을 읽기위해 스트림을 되감기함(rewind)
# write 작업을 하면 포인터는 파일의 끝에 위치함 이상태에서 open(read)를 하려면 읽을 게 없음 ;;;
stream.seek(0) 
image = Image.open(stream)
image.show()