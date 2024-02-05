'''
Name: Create a program that generates a Fibonacci sequence.
Author: @realJema 
Date: 10/2023
'''

def fibonacci(n): 
    if n < 0: 
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1: 
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(*[fibonacci(i) for i in range(10)])  # first 10 values in fibonacci series 