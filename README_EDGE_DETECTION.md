
# 🔍 Edge Detection (Phát hiện biên trong ảnh)

## 🧠 Mục tiêu
Tìm ra các đường ranh giới (biên) giữa các vật thể trong ảnh – nơi có sự thay đổi mạnh về cường độ (intensity) pixel.

---

## ⚙️ Các phương pháp chính

### 1. **Sobel Operator**
- Tính đạo hàm bậc nhất theo 2 hướng: ngang (Gx), dọc (Gy).
- Công thức biên độ:
  ```
  Magnitude = sqrt(Gx² + Gy²)
  ```

### 2. **Laplacian Operator**
- Tính đạo hàm bậc hai, phát hiện vùng chuyển sắc nhanh.

### 3. **Canny Edge Detection (phổ biến nhất)**
- Các bước:
  1. Làm mờ ảnh bằng Gaussian.
  2. Tính gradient theo Sobel.
  3. Non-maximum suppression (giảm nhiễu).
  4. Hysteresis Thresholding (lọc cạnh yếu/mạnh).

---

## 🧪 Code mẫu (Canny):
```python
import cv2
img = cv2.imread('image.jpg', 0)
edges = cv2.Canny(img, 100, 200)
cv2.imshow('Edges', edges)
```

---

## 📌 Ứng dụng
- Tách vật thể
- Nhận diện ký tự (OCR)
- Trích xuất đường biên trong xử lý ảnh y tế, bản đồ, ...
