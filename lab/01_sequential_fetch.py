import time
import requests
from utils import URLS, timer

@timer
def fetch_all_sequential(urls):
    results = []
    for url in urls:
        resp = requests.get(url)
        results.append(resp.text)
        print(f"Fetched {url} (len={len(resp.text)})")
    return results

if __name__ == "__main__":
    print("Running SEQUENTIAL fetch...")
    start = time.perf_counter()
    data = fetch_all_sequential(URLS)
    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds for {len(data)} requests")