import threading
import requests

def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

# Danh sách các URL để thực hiện yêu cầu
urls = ['https://example.com', 'https://example.org', 'https://example.net']

# Tạo và bắt đầu luồng
threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()
