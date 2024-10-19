import numpy as np

# 1. Đọc dữ liệu từ file heights_1.txt và weights_1.txt
with open('heights_1.txt') as f:
    height = [float(line.strip()) for line in f]  # Đọc và chuyển đổi thành số thực

with open('weights_1.txt') as f:
    weight = [float(line.strip()) for line in f]  # Đọc và chuyển đổi thành số thực

# 2. Tạo numpy array arr_height từ list height
arr_height = np.array(height)

# 3. Tạo numpy array arr_weight từ list weight
arr_weight = np.array(weight)

# 4. Chuyển đổi chiều cao từ inch sang mét (1 inch = 0.0254 m)
conversion_factor_height = 0.0254
arr_height_m = arr_height * conversion_factor_height

# 5. Chuyển đổi cân nặng từ pound sang kg (1 pound = 0.453592 kg)
conversion_factor_weight = 0.453592
arr_weight_kg = arr_weight * conversion_factor_weight

# 6. Tính BMI (BMI = weight (kg) / (height (m) ** 2))
arr_bmi = arr_weight_kg / (arr_height_m ** 2)

# 7. Giá trị cân nặng ở vị trí index = 50 trong arr_weight_kg
weight_at_index_50 = arr_weight_kg[50]

# 8. Tạo arr_height_m_100 với các phần tử có index từ 100 đến 110 (bao gồm 110)
arr_height_m_100 = arr_height_m[100:111]

# 9. Các cầu thủ có BMI < 21
players_bmi_below_21 = arr_bmi[arr_bmi < 21]

# 10. Chiều cao trung bình và cân nặng trung bình
average_height = np.mean(arr_height_m)
average_weight = np.mean(arr_weight_kg)

# 11. Chiều cao và cân nặng lớn nhất
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)

# 12. Chiều cao và cân nặng nhỏ nhất
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)

# In kết quả
print("Chiều cao ở vị trí index 50 (m):", arr_height_m[50])
print("Cân nặng ở vị trí index 50 (kg):", weight_at_index_50)
print("Chiều cao trung bình (m):", average_height)
print("Cân nặng trung bình (kg):", average_weight)
print("Chiều cao lớn nhất (m):", max_height)
print("Cân nặng lớn nhất (kg):", max_weight)
print("Chiều cao nhỏ nhất (m):", min_height)
print("Cân nặng nhỏ nhất (kg):", min_weight)
print("Chiều cao m từ index 100 đến 110:", arr_height_m_100)
print("Các cầu thủ có BMI < 21:", players_bmi_below_21)
