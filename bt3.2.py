import numpy as np

# Câu 1: Tạo numpy array arr có giá trị từ 0-9
arr = np.arange(10)
print("Array arr:", arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.size)

# Câu 2: Tạo arr_odd và arr_even từ array arr
arr_odd = arr[arr % 2 != 0]   # Các phần tử lẻ
arr_even = arr[arr % 2 == 0]  # Các phần tử chẵn
print("Array các phần tử lẻ (arr_odd):", arr_odd)
print("Array các phần tử chẵn (arr_even):", arr_even)

# Câu 3: Tạo arr_update_1 với phần tử chẵn giữ nguyên, phần tử lẻ thay bằng 100
arr_update_1 = np.where(arr % 2 == 0, arr, 100)
print("Array sau khi cập nhật (arr_update_1):", arr_update_1)
