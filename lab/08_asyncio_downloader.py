# 08_asyncio_downloader.py
import time
import asyncio
import aiohttp
from utils import URLS, timer

async def fetch(session, url):
    async with session.get(url) as resp:
        text = await resp.text()
        print(f"[ASYNC] Fetched {url} (len={len(text)})")
        return text

@timer
async def fetch_all_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    start = time.perf_counter()
    results = asyncio.run(fetch_all_async(URLS))
    end = time.perf_counter()
    print(f"Got {len(results)} responses in {end - start:.2f} sec")

    # This is like threading for I/O, but with coroutines instead of OS threads.
    # Scales better to huge numbers of concurrent I/O operations.