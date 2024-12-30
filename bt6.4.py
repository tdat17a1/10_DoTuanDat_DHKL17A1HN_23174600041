import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} is {result}")

# Tạo các luồng tính giai thừa
threads = []
for i in range(5, 8):  # Tính giai thừa cho 5, 6, 7
    thread = threading.Thread(target=factorial, args=(i,))
    threads.append(thread)
    thread.start()

# Chờ các luồng hoàn thành
for thread in threads:
    thread.join()
