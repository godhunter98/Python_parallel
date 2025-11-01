# 09_asyncio_http_downloader.py
import asyncio
import aiohttp
import time
from utils import URLS, timer

SEM_LIMIT = 5  # max 5 concurrent requests at a time

async def fetch_with_retry(session, url, attempt=1, max_attempts=3):
    try:
        async with session.get(url) as resp:
            text = await resp.text()
            return {"url": url, "ok": True, "len": len(text), "attempt": attempt}
    except Exception as e:
        if attempt < max_attempts:
            await asyncio.sleep(0.5)  # backoff
            return await fetch_with_retry(session, url, attempt+1, max_attempts)
        return {"url": url, "ok": False, "error": str(e), "attempt": attempt}

@timer
async def bounded_download(urls):
    sem = asyncio.Semaphore(SEM_LIMIT)
    async with aiohttp.ClientSession() as session:
        async def worker(u):
            async with sem:  # rate-limit concurrency
                result = await fetch_with_retry(session, u)
                print("Done:", result)
                return result
        tasks = [asyncio.create_task(worker(u)) for u in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.perf_counter()
    summary = asyncio.run(bounded_download(URLS))
    end = time.perf_counter()
    print(f"Finished {len(summary)} downloads in {end - start:.2f} sec")
    print("Sample result[0]:", summary[0])
    # Now you're doing:
    # - concurrency limit
    # - retry logic
    # - structured results