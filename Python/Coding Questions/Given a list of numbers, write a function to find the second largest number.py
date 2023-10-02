'''
Name: Given a list of numbers, write a function to find the second largest number.
Author: @realJema 
Date: 08/2023
'''

def second_largest(numbers): 
    # if the list is empty return none 
    if not numbers: 
        return None 
    
    # we sort the list 
    numbers.sort(reverse=True)

    # return the second element 
    return numbers[1]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 11, 63, -2, 39, 133, 174]
    print(second_largest(numbers))



    
