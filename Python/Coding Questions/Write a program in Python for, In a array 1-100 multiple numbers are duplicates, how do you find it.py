'''
Name: Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.
Author: @realJema 
Date: 06/2023
'''

numbers = list(range(1, 101)) + [42, 75, 88, 42]

duplicate_numbers = []

for num in numbers: # we go through the numbers list 
    if numbers.count(num) > 1: # check if numbers are duplicate with the count() function 
        if num not in duplicate_numbers: # we make sure we haven't already added the number to the array
            duplicate_numbers.append(num) # we add the number to the array 


print("The duplicate numbers are: ", duplicate_numbers)