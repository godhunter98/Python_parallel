import time
from concurrent.futures import ThreadPoolExecutor
import requests
from utils import URLS, timer


def fetch_one(url):
    resp = requests.get(url)
    print(f"[THREAD] Fetched {url} (len={len(resp.text)})")
    return resp    

if __name__ == "__main__":
    print("Running THREADED fetch...")
    start = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        result = [resp.text for resp in executor.map(fetch_one,URLS)]
    end = time.perf_counter()
    print(f"Total time: {end - start:.2f} seconds for {len(result)} requests")
    # Expect ~1-2 seconds, not ~10. This is your "wow" moment.