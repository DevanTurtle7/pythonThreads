import multiprocessing as mp
import math
import random
import time

NUM_ITERATIONS = 10000000

def benchmark(n, num_threads):
    avg = math.floor(NUM_ITERATIONS / num_threads)
    start = avg * n
    end = start + avg if n + 1 != num_threads else NUM_ITERATIONS
    
    for i in range(start, end):
        math.exp(random.random())

def time_trial(n):
    start_time = time.time()

    threads = []
    for i in range(0, n):
        thread = mp.Process(target=benchmark, args=(i, n))
        thread.start()
        threads.append(thread)

    for i in range(0, n):
        threads[i].join()

    end_time = time.time()
    print("Time taken with", n, "threads:", end_time - start_time)

if __name__ == "__main__":
    for i in range(1, 7):
        time_trial(i)
