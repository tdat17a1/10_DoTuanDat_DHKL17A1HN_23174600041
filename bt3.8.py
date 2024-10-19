import numpy as np

# Bước 1: Đọc dữ liệu từ file heights.txt và positions.txt
with open('heights.txt', 'r') as f:
    heights = [float(line.strip()) for line in f.readlines()]

with open('positions.txt', 'r') as f:
    positions = [line.strip() for line in f.readlines()]

# 1.a) Tạo numpy array từ positions
np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

# 1.b) Tạo numpy array từ heights
np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

# 2. Tính chiều cao trung bình của các GK
avg_height_gk = np.mean(np_heights[np_positions == 'GK'])
print("\nChiều cao trung bình của các GK:", avg_height_gk)

# 3. Tính chiều cao trung bình của những vị trí khác (Không phải là GK)
avg_height_others = np.mean(np_heights[np_positions != 'GK'])
print("Chiều cao trung bình của những vị trí khác:", avg_height_others)

# 4. Tạo mảng players với cấu trúc tự định nghĩa
players = np.array(list(zip(np_positions, np_heights)), dtype=[('position', 'U10'), ('height', 'f4')])

# 5. Sắp xếp players theo height
sorted_players = np.sort(players, order='height')
highest_player = sorted_players[-1]  # Chiều cao cao nhất
lowest_player = sorted_players[0]     # Chiều cao thấp nhất
print("\nVị trí có chiều cao cao nhất:", highest_player)
print("Vị trí có chiều cao thấp nhất:", lowest_player)
