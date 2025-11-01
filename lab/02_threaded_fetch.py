# 02_threaded_fetch.py
import time
import threading
import requests
from utils import URLS, timer

def fetch_one(url, results, index):
    resp = requests.get(url)
    results[index] = resp.text
    print(f"[THREAD] Fetched {url} (len={len(resp.text)})")

@timer
def fetch_all_threaded(urls):
    # pre-allocate list so each thread can drop result in correct slot
    results = [None] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        t = threading.Thread(target=fetch_one, args=(url, results, i))
        t.start()
        threads.append(t)

    # wait for all threads to finish
    for t in threads:
        t.join()

    return results

if __name__ == "__main__":
    print("Running THREADED fetch...")
    start = time.perf_counter()
    data = fetch_all_threaded(URLS)
    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds for {len(data)} requests")
    # Expect ~1-2 seconds, not ~10. This is your "wow" moment.