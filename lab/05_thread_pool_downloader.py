# 05_thread_pool_downloader.py
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from tqdm import tqdm
from utils import URLS, timer

def fetch(url):
    resp = requests.get(url)
    return url, resp.text

@timer
def fetch_all(urls, max_workers=10):
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(fetch, url): url for url in urls}

        for future in tqdm(as_completed(future_to_url), total=len(urls)):
            url, body = future.result()
            results[url] = body
    return results

if __name__ == "__main__":
    start = time.perf_counter()
    data = fetch_all(URLS)
    end = time.perf_counter()
    print(f"Downloaded {len(data)} pages in {end - start:.2f} sec")
    # Cleaner, scalable threading.