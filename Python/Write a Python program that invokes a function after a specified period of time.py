'''
Name: Write a Python program that invokes a function after a specified period of time. 
Author: @realJema 
Date: 01/2024
'''

import time 
import threading

def my_function(): 
    print("Hello, world!")

def main():
    # Set the time delay in seconds 
    delay = 2

    # Create a timer object 
    timer = threading.Timer(delay, my_function)
    timer.start()

    # wait for the timer to finish
    timer.join()

if __name__ == "__main__": 
    main()