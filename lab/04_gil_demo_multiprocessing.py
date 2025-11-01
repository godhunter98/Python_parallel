# 04_gil_demo_multiprocessing.py
import time
import multiprocessing
from utils import cpu_heavy

WORK = 5_000_000  # same as before

def run_cpu(label):
    start_time = time.perf_counter()
    cpu_heavy(WORK)
    end_time = time.perf_counter()
    print(f"{label} finished in {end_time - start_time:.2f} sec")

if __name__ == "__main__":
    print("Multiprocessing CPU tasks x2")
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=run_cpu, args=("Job A (proc)",))
    p2 = multiprocessing.Process(target=run_cpu, args=("Job B (proc)",))

    p1.start(); p2.start()
    p1.join(); p2.join()

    end = time.perf_counter()
    print(f"Total multiprocessing: {end - start:.2f} sec\n")

    print("Now you SHOULD see real speedup, because separate processes")
    print("= separate Python interpreters = not blocked by GIL.")