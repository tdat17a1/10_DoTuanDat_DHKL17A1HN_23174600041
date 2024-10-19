import numpy as np

# 1. Tạo array arr có kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Array arr (3x3 với giá trị True):\n", arr)

# 2. Tạo array 1D arr_ID và chuyển thành array 2D arr_2D
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape(3, 3)

# Chuyển cột 1 sang cột 3 và ngược lại
arr_2D[:, [1, 2]] = arr_2D[:, [2, 1]]
print("\nArray 2D sau khi chuyển cột 1 và cột 3:\n", arr_2D)

# 3. Chuyển dòng 1 sang dòng 2 và ngược lại
arr_2D[[0, 1]] = arr_2D[[1, 0]]
print("\nArray 2D sau khi chuyển dòng 1 và dòng 2:\n", arr_2D)

# 4. Đảo ngược các dòng của arr_2D
arr_2D_reversed_rows = arr_2D[::-1]
print("\nArray 2D sau khi đảo ngược các dòng:\n", arr_2D_reversed_rows)

# 5. Đảo ngược các cột của arr_2D
arr_2D_reversed_cols = arr_2D[:, ::-1]
print("\nArray 2D sau khi đảo ngược các cột:\n", arr_2D_reversed_cols)

# 6. Kiểm tra trong array arr_2D_null có giá trị null không
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\nCó giá trị NaN trong arr_2D_null:", has_nan)

# 7. Thay thế giá trị null bằng 0
arr_2D_null_filled = np.nan_to_num(arr_2D_null)
print("\nArray 2D null sau khi thay thế NaN bằng 0:\n", arr_2D_null_filled)
