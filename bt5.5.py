import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
connection = sqlite3.connect('my_database.db')

# Tạo bảng
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Chèn dữ liệu vào bảng
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Lấy tất cả các hàng từ bảng
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Dữ liệu trong bảng users:")
for row in rows:
    print(row)

# Lưu thay đổi và đóng kết nối
connection.commit()
connection.close()
