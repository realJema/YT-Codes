'''
Name:  counts the number of occurrences of each letter in a string:
Author: @realJema 
Date: 08/2023
''' 

def count_letters(string):
    char_count = {}

    for char in string: 
        if char in char_count: 
            char_count[char] += 1 
        else: 
            char_count[char] = 1

    for char, count in char_count.items():
        print(char, count)


# Example 
sentence = "Counts the number of occurrences of each letter in a string.py"
count_letters(sentence)