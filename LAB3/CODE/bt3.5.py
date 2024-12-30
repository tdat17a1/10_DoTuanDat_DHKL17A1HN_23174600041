import pandas as pd

# Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('DATA/stocks1.csv')
stocks2 = pd.read_csv('DATA/stocks2.csv')
stocks = pd.concat([stocks1, stocks2])

# 1. Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột date và symbol làm chỉ mục.
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, cho mỗi mã chứng khoán.
grouped_data = stocks.groupby(['date', 'symbol'])[['open', 'high', 'low', 'close', 'volume']].mean()

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán.
sorted_data = grouped_data.sort_index()

# Hiển thị kết quả cho 5 ngày đầu tiên.
print("\n5 dòng đầu tiên của dữ liệu sau khi sắp xếp theo ngày và mã chứng khoán:")
print(sorted_data.head())
