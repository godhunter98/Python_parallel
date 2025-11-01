# 07_lock_fixed_demo.py
import threading
from queue import Queue

counter = 0
lock = threading.Lock()

def increment_many(n_times, q: Queue):
    global counter
    for _ in range(n_times):
        with lock:
            counter += 1
    q.put("done")

if __name__ == "__main__":
    counter = 0
    N = 1_000_00
    q = Queue()

    t1 = threading.Thread(target=increment_many, args=(N, q))
    t2 = threading.Thread(target=increment_many, args=(N, q))

    t1.start(); t2.start()

    # show queue usage: wait for workers to signal
    msg1 = q.get()
    msg2 = q.get()

    t1.join(); t2.join()

    print("Worker signals:", msg1, msg2)
    print(f"Expected {2 * N}")
    print(f"Got      {counter}")
    print("Now it matches. Lock = serialize access safely.")