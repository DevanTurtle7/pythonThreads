"""
A random playground to mess around with threads and learn how they work in
python.

author: Devan Kavalchek
"""

import multiprocessing as mp
import math
import random
import time

def benchmark(thread, num_threads, num_operations):
    """
    A function that preforms many arbitrary operations so that are intensive
    on the system. The operations are split into chunks depending on how many
    threads are being used. These operations take a long time to complete
    (because there are so many), so that time differences are noticed between 
    different number of threads.

    Parameters:
        thread: The thread that is preforming this chunk of the work
        num_threads: The number of threads being used for this benchmark
        num_operations: The number of operations to be preformed
    """
    avg = math.floor(num_operations / num_threads) # Calculate the average work that should be done by 1 thread
    start = avg * thread # Get the starting index for the loop
    end = start + avg if thread + 1 != num_threads else num_operations # Calculate the ending index for the loop unless it is the last thread. If it is the last thread, assign the end to the end of the operations. This is because the end index calculation looses some numbers to rounding.
    
    for i in range(start, end): # Iterate the given amount of times
        math.exp(random.random()) # Preform an arbitrary operation

def time_trial(num_threads, num_operations):
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
        current = mp.Process(target=benchmark, args=(thread, num_threads, num_operations)) # Create a new thread
        current.start() # Start the thread
        threads.append(current) # Add the threads to the threads array

    # Wait for all the threads to finish
    for thread in threads: # Iterate over all the threads
        thread.join() # Wait for the thread to finish

    end_time = time.time() # Get the ending time
    time_taken = end_time - start_time # Get the time taken

    print("Time taken with", num_threads, "threads:", time_taken, "\n") # Print a message

def prompt_user(query):
    response = input(query)

    try:
        num = int(response)

        if num > 0:
            return num
        else:
            print("Invalid response. The number must be greater than 0.\n")
            return prompt_user(query)
    except:
        if response == "exit":
            return None
        else:
            print("Invalid response. Enter a number or type 'exit' to exit the program.\n")
            return prompt_user(query)

if __name__ == "__main__":
    exit = False
    
    num_operations = prompt_user("Enter a number of operations (suggested: 10000000): ")

    if (num_operations is None):
        exit = True

    while (not exit):
        num_threads = prompt_user("Enter the number of threads to test: ")

        if num_threads is not None:
            time_trial(num_threads, num_operations)
        else:
            exit = True
