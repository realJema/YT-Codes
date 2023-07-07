'''
Name: Write a program in Python to print the Fibonacci series using recursive method.
Code: AI Generated 
Author: @realJema 
Date: 06/2023
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i), end=", ")