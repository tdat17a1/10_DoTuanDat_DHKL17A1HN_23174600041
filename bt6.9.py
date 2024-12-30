import threading
import time

def thread_function(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"{name}: Web {time.strftime('%b %d %H:%M:%S %Y')}")
    time.sleep(1)
    print(f"Exiting {name}")

# Tạo và bắt đầu các luồng
threads = []
for name in ['Google', 'Yahoo', 'Facebook']:
    thread = threading.Thread(target=thread_function, args=(name,))
    threads.append(thread)
    thread.start()

# Chờ các luồng hoàn thành
for thread in threads:
    thread.join()

print("Exiting Main Thread")
