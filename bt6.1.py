import threading

def print_thread_name():
    print(f"Thread name: {threading.current_thread().name}")

# Tạo các luồng
threads = []
for i in range(5):
    thread = threading.Thread(target=print_thread_name)
    threads.append(thread)
    thread.start()

# Chờ các luồng hoàn thành
for thread in threads:
    thread.join()
