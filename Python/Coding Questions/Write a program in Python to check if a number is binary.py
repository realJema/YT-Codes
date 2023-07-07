'''
Name: Write a program in Python to check if a number is binary?
Author: @realJema - AI Assist 
Date: 06/2023
'''

def is_binary(num):
    binary = True 
    for digit in str(num):
        if digit != '0' and digit != '1':
            binary = False 
            break 
    return binary 

num = input("Enter a number : ")
if is_binary(num):
    print(num, "is a binary number.")
else: 
    print(num, "is not a binary number.")