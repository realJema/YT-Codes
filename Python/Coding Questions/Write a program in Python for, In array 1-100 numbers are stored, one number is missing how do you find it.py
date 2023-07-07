'''
Name: Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.
Author: @realJema 
Date: 06/2023
'''

# lets first create the array 
numbers = list(range(1, 101))

numbers.remove(int(input("Enter the missing number: "))) # we remove a number so we can find it 

total_sum = sum(numbers)

expected_sum = sum(range(1, 101))

missing_number = expected_sum - total_sum

print("The missing number is: ", missing_number)