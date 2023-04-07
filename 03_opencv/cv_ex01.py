import cv2

image_file = './sample_data/lena.jpg' # 실행되는 곳을 기준으로 (터미널에서 확인)
img = cv2.imread(image_file) # cv2.IMREAD_COLOR
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape)
print(img.dtype, img2.dtype)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

key = cv2.waitKey(5000)  # 5초기다리고 입력 없으면 -1 리턴
print(key)