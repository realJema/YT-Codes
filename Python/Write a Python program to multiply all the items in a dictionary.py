'''
Name: Write a Python program to multiply all the items in a dictionary.
Author: @realJema 
Date: 01/2024
'''

dictionary = {'key1' : 10, 'key2' : 2, 'key3' : 3}

# multiply all the items in the dictionary 
result = 1
for value in dictionary.values():
    result *= value

print (result)