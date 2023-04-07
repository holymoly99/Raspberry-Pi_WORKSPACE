


from time import sleep
import cv2


cap = cv2.VideoCapture(0)
frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

recording = False # 녹화 여부
recorder = None
def start_record():
    global recorder, recording
    start = datatime.now()
    fname = start.strftime('./sample_data/%Y%m%d_%H%M%S.mp4')
    recorder = cv2.VideoWriter(fname, fourcc, 20.0, frame_size)
    recording = True
    print(fname, 'start recording..')

def stop_record():
    global recorder, recording
    recording = False
    sleep(0.1) # 세그멘테이션 오류 방지
    recorder