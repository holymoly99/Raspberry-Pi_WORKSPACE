import cv2
import numpy as np

src = cv2.imread('./sample_data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
#임의의 각도로 회전시킬려면 getRotation뭐시기랑 또 무슨 함수해서, 총 2개 같이 써야함

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()