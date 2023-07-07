'''
Name: Write a program in Python to swap two numbers without using third variable?
Author: @realJema - AI Assist
Date: 06/2023
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping: num1 =", num1, "and num2 =", num2)

# we add both values into the first variable 
# then we set the second variable as the first one by subtracting its previous value from the now combined values 
# then we do the same for the first value 
num1 = num1 + num2 
num2 = num1 - num2 
num1 = num1 - num2 

print("After swapping: num1 =", num1, "and num2 =", num2) 
