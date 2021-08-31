import multiprocessing as mp
import math
import time

NUM_THREADS = 6
ASCII_START = 65
ASCII_END = 127

# the encrypt/decrypt function or whatever
def my_func(n):
    avg = math.floor((ASCII_END - ASCII_START) / NUM_THREADS)
    start = ASCII_START + (avg * n)
    end = start + avg if n + 1 != NUM_THREADS else ASCII_END

    for i1 in range(start, end):
        for i2 in range(ASCII_START, ASCII_END):
            for i3 in range(ASCII_START, ASCII_END):
                # do stuff
                pass

def thread_function(n):
    my_func(n)

if __name__ == "__main__":
    start_time = time.time()

    threads = []
    for i in range(0, NUM_THREADS):
        thread = mp.Process(target=thread_function, args=(i,))
        thread.start()
        threads.append(thread)

    for i in range(0, NUM_THREADS):
        threads[i].join()

    end_time = time.time()
    print("Time taken:", end_time - start_time)
