'''
Name: Write a program in Python to check whether a number is palindrome or not using recursive method.
Code: AI Generated 
Author: @realJema 
Date: 06/2023
'''

def is_palindrome(num):
    if len(str(num)) == 1:
        return True
    elif len(str(num)) == 2:
        return str(num)[0] == str(num)[1]
    else:
        return str(num)[0] == str(num)[-1] and is_palindrome(str(num)[1:-1])

# Example usage
num = 5554455555544555555445551
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")