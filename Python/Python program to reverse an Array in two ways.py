'''
Name: Python program to reverse an Array in two ways.
Author: @realJema 
Date: 10/2023
'''

def reverse_array_1(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array

def reverse_array_2(array):
    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

    return array  

# Example

array = [1, 2, 3, 4, 5]

reversed_array_1 = reverse_array_1(array)
reversed_array_2 = reverse_array_2(array)

print(reversed_array_1)
print(reversed_array_2)