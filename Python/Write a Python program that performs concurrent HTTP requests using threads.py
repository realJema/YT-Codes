'''
Name: Write a Python program that performs concurrent HTTP requests using threads.
Author: @realJema 
Date: 09/2023
'''

import threading
import requests

def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

# List of URLs to make requests to
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.python.org"
]

# Create threads for each URL
threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()