# 10_async_multiprocessing_pipeline.py
import asyncio
import aiohttp
import time
from concurrent.futures import ProcessPoolExecutor
from bs4 import BeautifulSoup  # you'll need: pip install beautifulsoup4
from utils import URLS, timer

# 1. Async fetch HTML
async def fetch_html(session, url):
    async with session.get(url) as resp:
        html = await resp.text()
        return {"url": url, "html": html}

async def fetch_all_html(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_html(session, u)) for u in urls]
        return await asyncio.gather(*tasks)

# 2. CPU-bound parse (we'll offload this to processes)
def extract_title(page_dict):
    html = page_dict["html"]
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string if soup.title else "(no title)"
    return {"url": page_dict["url"], "title": title}

@timer
def run_pipeline(urls):
    # Step A: async network
    html_pages = asyncio.run(fetch_all_html(urls))

    # Step B: CPU-heavy parsing in parallel processes
    with ProcessPoolExecutor() as pool:
        titles = list(pool.map(extract_title, html_pages))

    # Step C: final report
    for item in titles:
        print(f"{item['url']}  ->  {item['title']}")
    return titles

if __name__ == "__main__":
    start = time.perf_counter()
    report = run_pipeline(URLS)
    end = time.perf_counter()
    print(f"Full pipeline finished in {end - start:.2f} sec")
    print("This is real-world architecture: async I/O + CPU parallel parsing.")