'''
Name: Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
Author: @realJema 
Date: 09/2023
'''

class Stack: 
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty."
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
        

# Usage 
my_stack = Stack()
my_stack.push(10)
my_stack.push(30)

print("Size of stack: ", my_stack.size())
print("Popped item: ", my_stack.pop())
print("Popped item: ", my_stack.pop())

print("Is stack empty? ", my_stack.is_empty())