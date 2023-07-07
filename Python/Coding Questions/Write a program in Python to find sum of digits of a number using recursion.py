'''
Name: Write a program in Python to find sum of digits of a number using recursion?
Author: @realJema - AI assist 
Date: 06/2023
'''

# example: sum of 56 is 5 + 6 which is 11 

# function takes number as input and recursively finds the sum of its digits 
def sum_of_digits(num): 
    if num == 0: # checks if the number is 0 if yes returns zero
        return 0 
    else:  
        return (num % 10) + sum_of_digits(num // 10) # add last digit to the sum of the others recursively 

num = int(input("Enter a number: "))
sum = sum_of_digits(num)
print("The sum of digits of", num, "is", sum)
