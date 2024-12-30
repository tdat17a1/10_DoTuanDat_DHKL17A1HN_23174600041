import pandas as pd

# Đọc file companies.csv vào DataFrame companies.
companies = pd.read_csv('DATA/companies.csv')

# Hiển thị 5 dòng đầu tiên của companies.
print("5 dòng đầu tiên của companies:")
print(companies.head())

# Kết hợp stocks (đã tạo từ bài 3) và companies dựa trên cột chung là symbol.
stocks = pd.read_csv('DATA/stocks1.csv')
stocks2 = pd.read_csv('DATA/stocks2.csv')
stocks = pd.concat([stocks, stocks2])

# Kết hợp stocks và companies dựa trên cột 'symbol'
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name')

# Tính giá đóng cửa (close) trung bình cho mỗi công ty.
avg_close_price = merged_data.groupby('name')['close'].mean()

# Hiển thị kết quả cho 5 công ty đầu tiên.
print("\nGiá đóng cửa trung bình cho mỗi công ty:")
print(avg_close_price.head())
