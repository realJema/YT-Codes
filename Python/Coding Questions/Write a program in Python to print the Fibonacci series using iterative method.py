'''
Name: Write a program in Python to print the Fibonacci series using iterative method. - a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
Code: AI Generated 
Author: @realJema 
Date: 06/2023
'''

n = int(input("Enter the number of terms: "))

# initialize the first two terms
a, b = 0, 1

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto", n, ":")
   print(a)
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(a, end=", ")
       c = a + b
       # update values of a and b for the next iteration
       a, b = b, c