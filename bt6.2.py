import threading
import requests

def download_file(url):
    response = requests.get(url)
    with open(url.split('/')[-1], 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url}")

# Danh sách các URL để tải xuống
urls = ['https://example.com/file1', 'https://example.com/file2', 'https://example.com/file3']

# Tạo và bắt đầu luồng
threads = []
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()
