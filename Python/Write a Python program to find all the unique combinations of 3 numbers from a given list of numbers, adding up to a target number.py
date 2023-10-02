'''
Name: Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
Author: @realJema 
Date: 10/2023
'''

from itertools import combinations

def find_combinations(numbers, target):
    result = []
    for combination in combinations(numbers, 3):
        if sum(combination) == target: 
            result.append(combination)

    return result 

# Example 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
combinations = find_combinations(numbers, target)

print("Combinations adding up to", target, ":")
for combination in combinations:
    print(combination) 