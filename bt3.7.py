import numpy as np
# 1. Đọc dữ liệu từ file baseball_2D.txt vào list baseball
with open('baseball_2D.txt') as f:
    baseball = [list(map(float, line.strip().split())) for line in f]  # Đọc và chuyển đổi thành số thực

# 2. Tạo 2D numpy array np_baseball từ baseball
np_baseball = np.array(baseball)
print("\nKiểu dữ liệu của np_baseball:", np_baseball.dtype)
print("Kích thước của np_baseball:", np_baseball.shape)

# 3. In các giá trị của dòng thứ 50 trong np_baseball
print("\nGiá trị dòng thứ 50 trong np_baseball:", np_baseball[49])  # Lưu ý rằng chỉ số bắt đầu từ 0

# 4. Tạo numpy array np_weight với dữ liệu được lấy từ cột hai của np_baseball
np_weight = np_baseball[:, 1]

# 5. Chiều cao của vận động viên thứ 124
height_athlete_124 = np_baseball[123, 0]  # Chỉ số bắt đầu từ 0
print("\nChiều cao của vận động viên thứ 124:", height_athlete_124)

# 6. Chiều cao trung bình và cân nặng trung bình
average_height = np.mean(np_baseball[:, 0])
average_weight = np.mean(np_baseball[:, 1])
print("\nChiều cao trung bình:", average_height)
print("Cân nặng trung bình:", average_weight)

# 7. Nhận xét về tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print("\nHệ số tương quan giữa chiều cao và cân nặng:", correlation)

if correlation > 0:
    print("Tương quan thuận.")
elif correlation < 0:
    print("Tương quan nghịch.")
else:
    print("Không có tương quan.")
