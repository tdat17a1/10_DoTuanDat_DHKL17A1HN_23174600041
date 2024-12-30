import sqlite3

# Tạo kết nối tới cơ sở dữ liệu SQLite trong bộ nhớ
connection = sqlite3.connect(':memory:')

# Đóng kết nối
connection.close()
