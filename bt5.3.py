import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
connection = sqlite3.connect('my_database.db')

# Tạo một bảng trong cơ sở dữ liệu
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Lưu thay đổi và đóng kết nối
connection.commit()
connection.close()
