'''
Name: Write a Python program to find the maximum and minimum values in a set.
Author: @realJema 
Date: 10/2023
'''

def find_max_min_values(input_set):
    if len(input_set) == 0:
        return None, None 
    else: 
        max_value = max(input_set)
        min_value = min(input_set)
        return max_value, min_value
    

# Example 
my_set = {10, 5, 20, 15, 30}
max_value, min_value = find_max_min_values(my_set)

print("Maximum Value: ", max_value)
print("Minimum Value: ", min_value)