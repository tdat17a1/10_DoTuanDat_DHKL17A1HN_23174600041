import numpy as np

# 1. Đọc dữ liệu từ 2 tập tin efficiency.txt và shifts.txt
efficiency = np.loadtxt('efficiency.txt')
shifts = np.loadtxt('shifts.txt', dtype=str)

# 2. Tạo numpy array np_shifts và kiểm tra kiểu dữ liệu
np_shifts = np.array(shifts)
print(f"Kiểu dữ liệu của np_shifts: {np_shifts.dtype}")

# 3. Tạo numpy array np_efficiency và kiểm tra kiểu dữ liệu
np_efficiency = np.array(efficiency)
print(f"Kiểu dữ liệu của np_efficiency: {np_efficiency.dtype}")

# 4. Tính hiệu suất sản xuất trung bình của ca 'Morning'
morning_efficiency = np_efficiency[np_shifts == 'Morning']
print(f"Hiệu suất trung bình của ca 'Morning': {np.mean(morning_efficiency)}")

# 5. Tính hiệu suất sản xuất trung bình của các ca khác
other_shifts_efficiency = np_efficiency[np_shifts != 'Morning']
print(f"Hiệu suất trung bình của các ca khác: {np.mean(other_shifts_efficiency)}")

# 6. Tạo mảng dữ liệu có cấu trúc (Structure Array)
workers = np.core.records.fromarrays([np_shifts, np_efficiency], names='shift, efficiency')
print("Dữ liệu cấu trúc workers:\n", workers)

# 7. Sắp xếp mảng workers theo efficiency và xác định ca làm việc hiệu suất cao/thấp nhất
workers_sorted = np.sort(workers, order='efficiency')
print(f"Ca làm việc hiệu suất cao nhất: {workers_sorted[-1]}")
print(f"Ca làm việc hiệu suất thấp nhất: {workers_sorted[0]}")
