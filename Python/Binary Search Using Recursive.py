'''
Name: Binary Search Using Recursive
Author: @realJema 
Date: 10/2023
'''

def binary_search(arr, low, high, x):
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x)
        else: 
            return binary_search(arr, mid + 1, high, x)
        
    else: 
        return -1 
    
# Example 
arr = [22, 3, 4, 10, 40]
x = 22 # element to find 

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else: 
    print("Element is not present in array")