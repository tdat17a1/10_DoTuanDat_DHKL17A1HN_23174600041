import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
connection = sqlite3.connect('my_database.db')

# Cập nhật tất cả giá trị trong cột 'age'
cursor = connection.cursor()
cursor.execute("UPDATE users SET age = 35 WHERE name = 'Alice'")

# Lấy và hiển thị các bản ghi sau khi cập nhật
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Dữ liệu sau khi cập nhật:")
for row in rows:
    print(row)

# Lưu thay đổi và đóng kết nối
connection.commit()
connection.close()
