import cv2

# cap = cv2.VideoCapture('http://192.168.0.102:4747/video') # droid cam(or ip camera)
cap = cv2.VideoCapture(0) # 연결된 카메라 번호
# cap = cv2.VideoCapture('./sample_data/vtest.avi') # 상대 경로

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))    
print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(40)
    if key == 27: # ESC키 번호인 27 누르면 루프 탈출
        break

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()
