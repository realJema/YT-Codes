'''
Name: Write a program in Python to find greatest among three integers.
Code: AI Generated 
Author: @realJema 
Date: 06/2023
Description: In this program, we first take three integers as input from the user using the input() function. Then, we use a series of if statements to compare the three integers and find the greatest one. 
'''

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a > b and a > c: 
    print(f"{a} is the greatest integer.")
elif b > a and b > c: 
    print(f"{b} is the greatest integer.")
else: 
    print(f"{c} is the greatest integer.")

