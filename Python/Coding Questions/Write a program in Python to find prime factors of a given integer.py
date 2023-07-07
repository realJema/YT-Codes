'''
Name: Write a program in Python to find prime factors of a given integer.
Author: @realJema - AI Assist 
Date: 06/2023
'''


def prime_factors(num):
    factors = []
    divisor = 2 
    while divisor <= num:
        if num % divisor == 0: # we check if its divisble 
            factors.append(int(num)) # add the value into array 
            num = num / divisor 
        else: 
            divisor += 1  # we increment the divisor till we reach the num 
    return factors 

num = int(input("Enter a number: "))
print("The prime factors of", num, "are:", prime_factors(num))
