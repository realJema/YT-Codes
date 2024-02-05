'''
Name: What are lists and tuples? What is the key difference between the two?
Author: @realJema 
Date: 10/2023
'''

# Lists example 
# Lists are mutable 
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
fruits[1] = 'kiwi'
print(fruits) # Output: ['apple', 'kiwi', 'orange', 'grape']

# Tuples example
# Tuples are immutable 
colors = ('red', 'green', 'blue')
# colors.append('yellow') # Output: error 
# colors[1] = 'purple'  # Output: error 
print(colors) # Output: ('red', 'green', 'blue')