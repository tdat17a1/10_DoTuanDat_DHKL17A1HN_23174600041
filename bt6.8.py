import threading
import random

def sum_list_part(part_list):
    total = sum(part_list)
    print(f"Sum of {part_list} is {total}")
    return total

# Nhập số phần tử và số luồng
n = int(input("Nhập số phần tử: "))
num_threads = int(input("Nhập số luồng: "))

# Tạo danh sách ngẫu nhiên
lst = [random.randint(0, 10) for _ in range(n)]
print(f"List: {lst}")

# Chia danh sách thành các phần
chunk_size = n // num_threads
chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Tạo và bắt đầu các luồng
threads = []
for chunk in chunks:
    thread = threading.Thread(target=sum_list_part, args=(chunk,))
    threads.append(thread)
    thread.start()

# Chờ các luồng hoàn thành
for thread in threads:
    thread.join()
