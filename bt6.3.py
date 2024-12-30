import threading

def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"Even: {i}")

def print_odd_numbers():
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"Odd: {i}")

# Tạo luồng
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

# Bắt đầu luồng
even_thread.start()
odd_thread.start()

# Chờ luồng hoàn thành
even_thread.join()
odd_thread.join()
