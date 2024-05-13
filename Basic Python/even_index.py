'''
Name: Print characters from a string that are present at an even index number
Author: @realJema 
Date: 04/2024
'''

# Method 1 
word = input('Enter word: ')
print("Original String: ", word)
print("")

size = len(word) + 1 # add one since index starts at zero and not one 

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


# Method 2 
x = list(word) # convert word to list of chars 
for i in x[0::2]:
    print(i) 
