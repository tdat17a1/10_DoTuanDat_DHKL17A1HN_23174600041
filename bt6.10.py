import threading

def find_max_in_list(lst):
    max_value = max(lst)
    print(f"Max in {lst} is {max_value}")
    return max_value

# Tạo danh sách ngẫu nhiên
lst = [random.randint(0, 100) for _ in range(100)]

# Chia danh sách thành các phần
num_threads = 4
chunk_size = len(lst) // num_threads
chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Tạo và bắt đầu các luồng
threads = []
for chunk in chunks:
    thread = threading.Thread(target=find_max_in_list, args=(chunk,))
    threads.append(thread)
    thread.start()

# Chờ các luồng hoàn thành
for thread in threads:
    thread.join()
