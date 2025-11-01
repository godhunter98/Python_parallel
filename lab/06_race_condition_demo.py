# 06_race_condition_demo.py
import threading

counter = 0  # shared

def increment_many(n_times):
    global counter
    for _ in range(n_times):
        counter += 1  # <-- not atomic, can collide

if __name__ == "__main__":
    counter = 0
    N = 1_000_00

    t1 = threading.Thread(target=increment_many, args=(N,))
    t2 = threading.Thread(target=increment_many, args=(N,))

    t1.start(); t2.start()
    t1.join(); t2.join()

    print(f"Expected {2 * N}")
    print(f"Got      {counter}")
    print("If Got < Expected => race condition (threads stepped on each other)")