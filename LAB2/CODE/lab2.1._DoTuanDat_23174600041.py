#1. Tạo Dữ Liệu Mô Phỏng Nhiệt Độ (10 phút)
import numpy as np

# Tạo mảng nhiệt độ ngẫu nhiên từ 15.0 đến 35.0
temperature = np.round(np.random.uniform(15.0, 35.0, 30), 2)
print("Temperature Data:", temperature)

# Nhiệt độ trung bình trong tháng
average_temperature = np.mean(temperature)
print(f"Average Temperature: {average_temperature:.2f} °C")

#2. Phân Tích Xu Hướng Nhiệt Độ (5-10 phút)
# Ngày có nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperature)
min_temp = np.min(temperature)
day_max = np.argmax(temperature) + 1  # Cộng 1 để chỉ ngày thực tế
day_min = np.argmin(temperature) + 1

print(f"Highest temperature: {max_temp} °C on day {day_max}")
print(f"Lowest temperature: {min_temp} °C on day {day_min}")

# Tính sự thay đổi nhiệt độ giữa các ngày
temp_diff = np.abs(np.diff(temperature))
max_diff_day = np.argmax(temp_diff) + 1
print(f"Day with the highest temperature change: Day {max_diff_day} with a change of {temp_diff[max_diff_day - 1]} °C")

#3. Áp dụng Fancy Indexing (10 phút)
# Các ngày có nhiệt độ cao hơn 20°C
above_20 = temperature[temperature > 20]
print(f"Days with temperature above 20°C: {above_20}")

# Nhiệt độ của các ngày 5, 10, 15, 20, và 25
selected_days = temperature[[4, 9, 14, 19, 24]]
print(f"Temperatures on days 5, 10, 15, 20, 25: {selected_days}")

# Nhiệt độ của các ngày có nhiệt độ cao hơn trung bình
above_average = temperature[temperature > average_temperature]
print(f"Temperatures above average: {above_average}")

# Nhiệt độ của các ngày chẵn và lẻ
even_days_temp = temperature[::2]
odd_days_temp = temperature[1::2]
print(f"Temperatures on even days: {even_days_temp}")
print(f"Temperatures on odd days: {odd_days_temp}")
