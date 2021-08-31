"""
A random playground to mess around with threads and learn how they work in
python.

author: Devan Kavalchek
"""

import multiprocessing as mp
import math
import random
import time

NUM_ITERATIONS = 10000000 # The number of iterations/operations in a benchmark

def benchmark(thread, num_threads):
    """
    A function that preforms many arbitrary operations so that are intensive
    on the system. The operations are split into chunks depending on how many
    threads are being used. These operations take a long time to complete
    (because there are so many), so that time differences are noticed between 
    different number of threads.

    Parameters:
        thread: The thread that is preforming this chunk of the work
        num_threads: The number of threads being used for this benchmark
    """
    avg = math.floor(NUM_ITERATIONS / num_threads)
    start = avg * thread
    end = start + avg if thread + 1 != num_threads else NUM_ITERATIONS
    
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
