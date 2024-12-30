import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
connection = sqlite3.connect('my_database.db')

# Xóa một hàng cụ thể khỏi bảng
cursor = connection.cursor()
cursor.execute("DELETE FROM users WHERE name = 'Bob'")

# Lấy và hiển thị các bản ghi sau khi xóa
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Dữ liệu sau khi xóa:")
for row in rows:
    print(row)

# Lưu thay đổi và đóng kết nối
connection.commit()
connection.close()
