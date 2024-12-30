import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
connection = sqlite3.connect('my_database.db')

# Đếm số bản ghi trong bảng
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM users")
record_count = cursor.fetchone()[0]
print(f"Số lượng bản ghi trong bảng users: {record_count}")

# Đóng kết nối
connection.close()
