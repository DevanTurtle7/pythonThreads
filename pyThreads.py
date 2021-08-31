"""
A random playground to mess around with threads and learn how they work in
python. It is currently a command line interface to test different thread
counts with different numbers of operations.

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
    """
    Prompts a user to enter a number

    Parameters:
        query: A message that will display to the user when prompting them
    """
    response = input(query).lower() # Prompt the user and convert their response to lowercase

    try:
        num = int(response) # Convert the response to an integer

        if num > 0: # Check if the number is greater than 0
            return num # Return the number that the user entered
        else:
            print("Invalid response. The number must be greater than 0.\n") # Print a message to the user
            return prompt_user(query) # Prompt the user again
    except: # The response was not an integer
        if response == "exit": # Check if the user entered the exit command
            return None # Return None (exit the program)
        elif response == "coperations": # Check if the user entered the coperations command
            return -1 # Return -1
        elif response == "help": # Check if the user entered the help command
            print("Commands:\n\tcoperations: Prompts you to change the number of operations\n\texit: Exits the program\n\thelp: list all of the commands\n") # Print a list of commands to the user
            return prompt_user(query) # Prompt the user again
        else:
            print("Invalid response. Enter a number or type 'exit' to exit the program.\n") # Print a message to the user
            return prompt_user(query) # Prompt the user again

if __name__ == "__main__":
    exit = False # Keeps track of if the program should exit or not
    
    num_operations = prompt_user("Enter a number of operations (suggested: 10000000): ") # Prompt the user to enter the number of operations

    if (num_operations is None): # Check if the user entered the exit command
        exit = True # Exit the program

    while (not exit): # Loop until the user exits
        num_threads = prompt_user("Enter the number of threads to test: ") # Prompt the user to enter a number of threads to test

        if num_threads is None: # Check if the user entered the exit command
            exit = True # Exit the program
        elif num_threads == -1: # Check if the user entered the coperations command
            num_operations = prompt_user("Enter a number of operations (suggested: 10000000): ") # Prompt the user to enter the number operations
        else:
            time_trial(num_threads, num_operations) # Run a time trial for the given number of threads and operations
