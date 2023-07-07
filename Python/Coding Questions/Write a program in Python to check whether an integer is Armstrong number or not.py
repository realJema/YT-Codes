'''
Name: Write a program in Python to check whether an integer is Armstrong number or not.
Code: AI Generated 
Author: @realJema 
Date: 06/2023
'''

num = int(input("Enter a number: "))

# determine the number of digits
num_digits = len(str(num))

# initialize sum
sum = 0

# calculate sum of nth power of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

# check if the number is Armstrong or not
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")