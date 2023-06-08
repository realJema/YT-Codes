'''
Name: Write a program to reverse an integer in Python
Code: AI Generated 
Author: @realJema 
Date: 06/2023
'''

num = int(input("Enter an integer: "))  # take input from user

rev = 0  # initialize reversed integer to 0

while num > 0:  # loop until the input integer becomes 0
    rem = num % 10  # get the last digit of the input integer
    rev = (rev * 10) + rem  # append the last digit to the reversed integer
    num = num // 10  # remove the last digit from the input integer

print("Reversed integer:", rev)  # print the reversed integer