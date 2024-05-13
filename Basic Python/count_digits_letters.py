'''
Name: Write a Python program that accepts a string and calculates the number of digits and letters.
Author: @realJema 
Date: 04/2024
'''


s = input("Enter a statement: ")
digits = 0
letters = 0 

for i in s: 
    if i.isdigit(): 
        digits += 1 
    elif i.isalpha(): 
        letters += 1 
    else: 
        continue 

print(f"Number of letters: {letters}, Number of digits: {digits}")
