'''
Name: Write a Python program to create multiple threads and print their names.
Author: @realJema 
Date: 09/2023
'''

import threading 

def print_thread_name(): 
    print("Thread name: ", threading.current_thread().name)


thread1 = threading.Thread(target=print_thread_name, name="Thread 1")
thread2 = threading.Thread(target=print_thread_name, name="Thread 2")
thread3 = threading.Thread(target=print_thread_name, name="Thread 3")

# Start the threads 
thread1.start()
thread2.start()
thread3.start()