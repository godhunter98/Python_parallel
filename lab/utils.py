# utils.py
import time
import random

# We'll "pretend" these are expensive network calls.
URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
]

def cpu_heavy(n: int) -> int:
    """
    Intentionally dumb CPU-heavy task.
    We'll sum a bunch of random multiplications.

    This is just to burn CPU, not to be clever.
    """
    total = 0
    for _ in range(n):
        a = random.randint(1, 10_000)
        b = random.randint(1, 10_000)
        total += a * b
    return total


def timer(fn):
    """Decorator to time a function call and print duration."""
    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        print(f"[TIMER] {fn.__name__} took {end - start:.2f} seconds")
        return result
    return wrapped