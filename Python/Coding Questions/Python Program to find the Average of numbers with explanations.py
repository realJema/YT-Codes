'''
Name: Python Program to find the Average of numbers with explanations.
Author: @realJema - AI Assist 
Date: 07/2023
'''

num_str = input("Enter numbers separated by spaces: ") # get input from user with all numbers 

num_list = num_str.split() # we get all individual numbers into a list 

num_list = [int(num) for num in num_list] # convert the list of strings to a list of integers 

total = sum(num_list)

average = total / len(num_list)

print("The average is: ", average) 