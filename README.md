# Py Concurrency Lab

A hands-on path from “one slow loop” to multiprocessing pipelines. These are the exact exercises I used to understand Python concurrency; now you can follow the same sequence (or teach it on YouTube).

## Prerequisites

- Python 3.12+
- `pip` (or [astral-sh/uv](https://github.com/astral-sh/uv) if you prefer a faster installer)
- Optional: `python -m pip install pipx` if you want isolated tool installs

Install dependencies once:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # or `pip install -e .` to use pyproject.toml
```

(If you use `uv`, swap the last line for `uv pip install -r requirements.txt`.)

## Repo Layout

- `basics/` – bite-sized scripts that answer “what changes when I add threads or processes?”
- `lab/` – fuller demos that combine networking, CPU work, locks, async, and multiprocessing
- `main.py` – intentionally empty; leave it for your own experiments or live-coding

Each script is isolated so you can run it, show the output, and reset the terminal before the next clip.

## Suggested Teaching Flow

1. **Baseline intuition (basics/)**
   - `0_sequential.py`: one process, lots of waiting. Perfect “before” benchmark.
   - `1_multiprocess.py`: drop-in `ProcessPoolExecutor` replacement; highlight CPU parallelism.
   - `2_single_threaded.py` → `3_multi_threaded.py`: same network workload, now “fast” thanks to threads.

2. **I/O concurrency in depth (lab/01–05)**
   - `01_sequential_fetch.py`: narrate “URL #1… still waiting…”
   - `02_threaded_fetch.py`: introduce threads, talk about `GIL` irrelevance for blocking I/O.
   - `05_thread_pool_downloader.py`: cleaner abstraction + progress bar with `tqdm`.

3. **CPU-bound reality check (lab/03–04)**
   - `03_gil_demo_threads.py`: threads don’t help CPU-heavy work.
   - `04_gil_demo_multiprocessing.py`: processes beat the GIL; show timings side by side.

4. **Race conditions & synchronization (lab/06–07)**
   - `06_race_condition_demo.py`: demo the “expected vs got” mismatch.
   - `07_lock_fixed_demo.py`: introduce `Lock` and `Queue` to show safe coordination.

5. **Asyncio for scale (lab/08–10)**
   - `08_asyncio_downloader.py`: translate the threading idea into coroutines.
   - `09_asyncio_http_downloader.py`: add retry logic and concurrency limits with semaphores.
   - `10_async_multiprocessing_pipeline.py`: finish with a hybrid pipeline (async fetch + process pool parsing using BeautifulSoup).

## How to Run a Demo

```bash
source .venv/bin/activate
python basics/1_multiprocess.py
python lab/02_threaded_fetch.py
python lab/07_lock_fixed_demo.py
python lab/10_async_multiprocessing_pipeline.py
```

When recording, keep one script per segment; reset the terminal clock so viewers can see the time difference each time.

## Teaching Tips & B-Roll Ideas

- Start each clip with the slow version so the win feels obvious.
- Print elapsed time (`perf_counter`) in every script—already built-in.
- Keep `WORK = 5_000_000` in the CPU demos, but mention viewers can tune it if their laptop is faster/slower.
- For the async episodes, open two terminals: one running the script, another showing an `htop` or `Activity Monitor` view of CPU usage.
- Close with `10_async_multiprocessing_pipeline.py` to recap: “Threads for I/O, processes for CPU, async for scale, locks for safety.”

## Extending the Lab

- Swap `httpbin` URLs for your own API.
- Add CLI arguments (threads vs processes) to experiment live.
- Wire up `pytest-benchmark` if you want more formal numbers for a follow-up video.

---

Copy this Markdown into `README.md` and you’re ready to go. Natural next step: record your first video chapter while the commands are fresh.
