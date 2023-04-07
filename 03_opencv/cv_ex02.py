import cv2

image_file = './sample_data/lena.jpg'
img = cv2.imread(image_file)

cv2.imwrite('./sample_data/Lena.bmp', img)
cv2.imwrite('./sample_data/Lena.png', img)
cv2.imwrite('./sample_data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./sample_data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite('./sample_data/Lena4.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 1])
