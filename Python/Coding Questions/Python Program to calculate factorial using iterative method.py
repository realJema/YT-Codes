'''
Name: Python Program to calculate factorial using iterative method.
Author: @realJema 
Date: 07/2023
'''

# Factorial of 3 is 3 * 2 * 1 = 6
num = int(input("Enter a number: "))

factorial = 1 

for i in range(1, num +1 ):
    factorial *= i 

print("The factorial of", num, "is: ", factorial)