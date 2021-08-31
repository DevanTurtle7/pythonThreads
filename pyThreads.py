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
    avg = math.floor(NUM_ITERATIONS / num_threads) # Calculate the average work that should be done by 1 thread
    start = avg * thread # Get the starting index for the loop
    end = start + avg if thread + 1 != num_threads else NUM_ITERATIONS # Calculate the ending index for the loop unless it is the last thread. If it is the last thread, assign the end to the end of the operations. This is because the end index calculation looses some numbers to rounding.
    
    for i in range(start, end): # Iterate the given amount of times
        math.exp(random.random()) # Preform an arbitrary operation

def time_trial(num_threads):
    """
    Preforms a timed trial of the benchmark function using a given number of
    threads.

    Parameters:
        num_threads: The number of threads being used for this time trial
    """
    start_time = time.time() # Get the current time
    threads = [] # Create an array to store the threads, so that the program can wait for all of them to finish

    # Create and start the given number of threads
    for thread in range(0, num_threads): # Iterate num_threads times
        current = mp.Process(target=benchmark, args=(i, num_threads)) # Create a new thread
        current.start() # Start the thread
        threads.append(current) # Add the threads to the threads array

    # Wait for all the threads to finish
    for thread in threads: # Iterate over all the threads
        thread.join() # Wait for the thread to finish

    end_time = time.time() # Get the ending time
    time_taken = end_time - start_time # Get the time taken

    print("Time taken with", num_threads, "threads:", time_taken) # Print a message

if __name__ == "__main__":
    for i in range(1, 7): # Create 6 threads
        time_trial(i) # Run a time trial with i threads
