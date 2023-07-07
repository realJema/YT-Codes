'''
Name: Python Program to convert Decimal number to Octal number.
Author: @realJema 
Date: 06/2023
'''

decimal = int(input("Enter a decimal number: "))

octal = oct(decimal).replace("0o", "")

print("The ocatal representation of", decimal, "is:", octal)
