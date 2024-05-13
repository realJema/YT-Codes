'''
Name: Write a python program to count the number of even and odd numbers in a series of numbers
Author: @realJema 
Date: 04/2024
'''

numbers = (1, 2, 3, 4, 5, 7, 8, 9)

c_odd = 0 
c_even = 0 

for number in range(0, 1000): 
    if number % 2 == 0: 
        c_even += 1 
    else: 
        c_odd += 1 

print(f"Even numbers count: {c_even}, Odd numbers count: {c_odd}")
