'''
Name: Write a Python program to select a string from a given list of strings with the most unique characters.
Author: @realJema 
Date: 08/2023
'''

def string_with_most_unique_chars(lst):
    most_unique_string = ""
    most_unique = 0
    for string in lst:
        unique_chars = set(string)
        if len(unique_chars) > most_unique:
            most_unique = len(unique_chars)
            most_unique_string = string 
    return most_unique_string

if __name__ == "__main__":
    lst = ["hello", "world", "unique", "cher", "string"]
    print(string_with_most_unique_chars(lst))