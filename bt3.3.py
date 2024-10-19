import numpy as np

# Câu 1: Tạo arr_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1
print("arr_zeros:", arr_zeros)

# Câu 2: Tạo arr_h có giá trị từ 10 đến 24, in theo thứ tự đảo ngược
arr_h = np.arange(10, 25)
arr_h_reversed = arr_h[::-1]
print("arr_h (đảo ngược):", arr_h_reversed)

# Câu 3: Tạo arr_1 từ arr_k với các phần tử khác 0
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]
print("arr_1 (các phần tử khác 0):", arr_1)

# Câu 4: Thêm 2 phần tử 10 và 20 vào cuối array arr_1
arr_1_extended = np.append(arr_1, [10, 20])
print("arr_1 sau khi thêm 10 và 20:", arr_1_extended)

# Câu 5: Thêm phần tử có giá trị 100 vào vị trí index = 5
arr_1_extended = np.insert(arr_1_extended, 5, 100)
print("arr_1 sau khi thêm 100 vào index 5:", arr_1_extended)

# Câu 6: Xóa các phần tử tại vị trí index = 0, 1, 2
arr_final = np.delete(arr_1_extended, [0, 1, 2])
print("arr_final sau khi xóa index 0, 1, 2:", arr_final)
