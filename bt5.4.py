import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
connection = sqlite3.connect('my_database.db')

# Liệt kê các bảng
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Các bảng trong cơ sở dữ liệu SQLite:")
for table in tables:
    print(table[0])

# Đóng kết nối
connection.close()
