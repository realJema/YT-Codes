'''
Name: Write a program to confirm valid emails 
Author: @realJema 
Date: 08/2023
'''

import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'

    if re.match(regex, email):
        return "Valid Email" 
    else: 
        return "Invalid Email" 
    
if __name__ == "__main__":
    email = input("Enter your email : ")
    print(validate_email(email))

