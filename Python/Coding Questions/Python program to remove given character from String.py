'''
Name: Python program to remove given character from String.
Author: @realJema 
Date: 06/2023
'''

string = input("Enter a string: ")
character = input("Enter the character to remove: ")

new_string = string.replace(character, "")

print("Updated string: ", new_string)