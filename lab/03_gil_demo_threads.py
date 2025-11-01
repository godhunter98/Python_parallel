# 03_gil_demo_threads.py
import time
import threading
from utils import cpu_heavy

WORK = 5_000_000  # increase if it's too fast

def run_cpu(label):
    start = time.perf_counter()
    cpu_heavy(WORK)
    end = time.perf_counter()
    print(f"{label} finished in {end - start:.2f} sec")

if __name__ == "__main__":
    print("Sequential CPU tasks x2")
    start = time.perf_counter()
    run_cpu("Job A")
    run_cpu("Job B")
    end = time.perf_counter()
    print(f"Total sequential: {end - start:.2f} sec\n")

    print("Threaded CPU tasks x2")
    start = time.perf_counter()
    t1 = threading.Thread(target=run_cpu, args=("Job A (threaded)",))
    t2 = threading.Thread(target=run_cpu, args=("Job B (threaded)",))
    t1.start(); t2.start()
    t1.join(); t2.join()
    end = time.perf_counter()
    print(f"Total threaded: {end - start:.2f} sec\n")

    print("Observation: For CPU-heavy stuff, threaded ~= sequential.")
    print("Reason: the GIL only lets one Python thread execute Python bytecode at a time.")