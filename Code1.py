import cv2
import numpy as np

# Đọc ảnh và chuyển sang ảnh xám
image = cv2.imread('D:/download/1045-2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Bước 1: Tính toán góc Harris
# cv2.cornerHarris() trả về ma trận độ sáng (response) cho từng pixel trong ảnh
dst = cv2.cornerHarris(gray, 3, 3, 0.04)

# Bước 2: Tăng cường kết quả để dễ nhìn thấy các góc
# Dễ dàng nhận diện các góc trong ảnh bằng cách sử dụng ngưỡng
dst = cv2.dilate(dst, None)  # Tăng cường độ sáng tại các điểm góc

# Bước 3: Đánh dấu các góc trong ảnh
# Nếu giá trị trong ma trận độ sáng lớn hơn ngưỡng 0.01 lần giá trị lớn nhất của ma trận, đánh dấu đó là góc
image[dst > 0.01 * dst.max()] = [0, 0, 255]

# Hiển thị kết quả
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
