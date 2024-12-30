import threading

def print_even_numbers_up_to(n):
    for i in range(2, n + 1, 2):
        print(f"Even: {i}")

def print_odd_numbers_up_to(n):
    for i in range(1, n + 1, 2):
        print(f"Odd: {i}")

# Tạo và bắt đầu luồng
n = 20
even_thread = threading.Thread(target=print_even_numbers_up_to, args=(n,))
odd_thread = threading.Thread(target=print_odd_numbers_up_to, args=(n,))

even_thread.start()
odd_thread.start()

# Chờ các luồng hoàn thành
even_thread.join()
odd_thread.join()
