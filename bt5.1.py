import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite (nếu cơ sở dữ liệu chưa tồn tại, nó sẽ được tạo)
connection = sqlite3.connect('my_database.db')

# Lấy phiên bản của SQLite
cursor = connection.cursor()
cursor.execute('SELECT SQLITE_VERSION()')
sqlite_version = cursor.fetchone()
print(f"SQLite version: {sqlite_version[0]}")

# Đóng kết nối
connection.close()
