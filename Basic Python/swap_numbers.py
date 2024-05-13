'''
Name:  Program to swap first and last element of a list 
Author: @realJema 
Date: 04/2024
'''

# Method 1 
def swapList(newList):
    size = len(newList) 

    # swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp 

    return newList 

# Example 
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# Method 2 
def swapList2(newList):

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

newList2 = [12, 35, 9, 56, 24]
print("")
print(swapList2(newList2))


# Method 3 
def swapList3(list): 
    start, *middle, end = list 
    list = [end, *middle, start]

    return list 

newList3 = [12, 35, 9, 56, 24]
print(swapList3(newList3))

# Method 4 
def swapList4(list): 

    first = list.pop(0)
    last = list.pop(-1) 

    list.insert(0, last)
    list.append(first)

    return list 


newList4 = [12, 35, 9, 56, 24]
print(swapList4(newList4))
