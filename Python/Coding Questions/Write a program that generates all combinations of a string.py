'''
Name: Write a program that generates all combinations of a string.
Author: @realJema 
Date: 08/2023
'''

def generate_combinations(string):
    if len(string) == 0: 
        return "empty string"
    
    combinations = []
    for i in range(len(string)):
        first_letter = string[i]
        remaining_letters = string[i+1:]
        combinations_of_remaining_letters = generate_combinations(remaining_letters)
        for combination in combinations_of_remaining_letters:
            combinations.append(f'{first_letter}{combination}')
            combinations.append(first_letter)

    return combinations 

if __name__ == '__main__':
    print(generate_combinations('abc'))

    