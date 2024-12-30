import pandas as pd

# Đọc file stocks1.csv vào DataFrame stocks1.
stocks1 = pd.read_csv('DATA/stocks1.csv')

# 1. Kiểm tra xem trong stocks1 có dữ liệu Null nào không.
print("\nKiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())

# 2. Thay thế dữ liệu Null ở cột high bằng giá trị trung bình của cột high.
stocks1['high'].fillna(stocks1['high'].mean(), inplace=True)

# 3. Thay thế dữ liệu Null ở cột low bằng giá trị trung bình của cột low.
stocks1['low'].fillna(stocks1['low'].mean(), inplace=True)

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null.
print("\nThông tin tổng quan sau khi xử lý Null:")
print(stocks1.info())
