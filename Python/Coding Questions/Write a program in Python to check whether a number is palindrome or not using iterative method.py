'''
Name: Write a program in Python to check whether a number is palindrome or not using iterative method. - a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.
Code: AI Generated 
Author: @realJema 
Date: 06/2023
'''

def is_palindrome(num):
    # Convert the number to a string
    str_num = str(num)
    
    # Iterate over the string from both ends
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-i - 1]:
            return False
    
    return True

# Example usage
print(is_palindrome(11111111112111111111))  # True
print(is_palindrome(111111111121111111111))  # False