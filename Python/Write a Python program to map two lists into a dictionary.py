'''
Name: Write a Python program to map two lists into a dictionary.
Author: @realJema 
Date: 01/2024
'''

# create two lists 
keys = ['key1', 'key2', 'key3']
values = ['value1', 'value2', 'value3']

# create a dictionary from the two lists 
dictionary = dict(zip(keys, values))

# printing the dictionary 
print(dictionary) 