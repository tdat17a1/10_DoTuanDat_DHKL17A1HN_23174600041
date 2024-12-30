import pandas as pd

# 1. Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('DATA/stocks1.csv')
stocks2 = pd.read_csv('DATA/stocks2.csv')

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks.
stocks = pd.concat([stocks1, stocks2])

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày.
average_prices = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

# 4. Hiển thị 5 dòng đầu tiên của kết quả.
print("\n5 dòng đầu tiên của giá trung bình mỗi ngày:")
print(average_prices.head())
