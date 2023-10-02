'''
Name:  Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Author: @realJema 
Date: 08/2023
'''

def check_list(lst):
    length = len(lst)
    fifth_element = lst[4]
    count_fifth = lst.count(fifth_element)
    if length == 8 and count_fifth == 3: 
        return True 
    else: 
        return False 
    

# Example usage 
numbers = [1, 2, 3, 4, 5, 5, 5, 6]
numbers2 = [1, 2, 3, 5, 5, 6] # fifth elemetn is 5 and occurs only twice 
numbers3 = [1, 2, 3, 4, 1, 5, 5, 1]
print("Test 1 : ", check_list(numbers))
print("Test 2 : ", check_list(numbers2))
print("Test 3 : ", check_list(numbers3))