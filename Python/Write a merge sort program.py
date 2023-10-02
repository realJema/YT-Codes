'''
Name: Write a merge sort program.
Author: @realJema 
Date: 08/2023
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else: 
            result.append(right[j])
            j += 1 
    
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result 

# Example 
array = [8, 4, 2, 9, 5, 1, 6, 3, 7]
sorted_array = merge_sort(array)
print(sorted_array)