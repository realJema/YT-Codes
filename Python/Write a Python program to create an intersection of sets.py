'''
Name: Write a Python program to create an intersection of sets.
Author: @realJema 
Date: 10/2023
'''

def find_intersection(set1, set2):
    intersection = set1.intersection(set2)
    return intersection

# Example 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
intersection = find_intersection(set1, set2)

print("Intersection: ", intersection)
