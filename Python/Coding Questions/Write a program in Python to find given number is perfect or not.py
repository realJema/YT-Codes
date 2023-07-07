'''
Name: Write a program in Python to find given number is perfect or not?
Author: @realJema - AI Assist
Date: 06/2023
'''


'''
Example: In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number. Wikipedia
'''

def is_perfect(num):
    sum = 0 
    for i in range(1, num):
        if num % i == 0:
            sum += i 
    if sum == num:
        return True 
    else: 
        return False 

num = int(input("Enter a number: "))
if is_perfect(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")