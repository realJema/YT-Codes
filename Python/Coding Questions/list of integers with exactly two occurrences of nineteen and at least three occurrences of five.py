'''
Name:  Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Author: @realJema 
Date: 08/2023
'''

def check_occurences(lst):
    count_nineteen = lst.count(19)
    count_five = lst.count(5)

    if count_nineteen == 2 and count_five >= 3:
        return True 
    else: 
        return False 
    

# Test Cases 
print("Test 1 : ", check_occurences([5, 19, 5, 19, 5, 5, 10, 19])) # more than 2 values of 19
print("Test 2 : ", check_occurences([5, 19, 5, 5, 10, 19])) # meets condition 
print("Test 3 : ", check_occurences([5, 19, 5, 19, 5, 19])) # more than 2 values of 19 