'''
name: Pass_generator.py
author: realjema
date: 01/2023
'''

import random 

password_length = int(input("enter the length of password : ")) # ask the user for length of password 

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" # all characters to use 

password = "".join(random.sample(characters, password_length)) # gets a random character for the numbers of times defined by length

print(password) 

# with this program you can easily generate strong passwords 