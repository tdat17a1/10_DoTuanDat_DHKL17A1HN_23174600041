import pandas as pd

# Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('DATA/stocks1.csv')
stocks2 = pd.read_csv('DATA/stocks2.csv')
stocks = pd.concat([stocks1, stocks2])

# 1. Tạo Pivot Table từ DataFrame stocks với date làm chỉ mục, symbol làm cột, và giá trị trung bình của close làm giá trị.
pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')

# 2. Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol).
total_volume = pd.pivot_table(stocks, values='volume', index='date', columns='symbol', aggfunc='sum')
pivot_table['total_volume'] = total_volume.sum(axis=0)

# 3. Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp.
pivot_table_sorted = pivot_table.sort_values(by='total_volume', axis=1, ascending=False)

# Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất.
print("\n5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(pivot_table_sorted.head())
