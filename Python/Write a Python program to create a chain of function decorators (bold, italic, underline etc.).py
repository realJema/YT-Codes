'''
Name: Write a Python program to create a chain of function decorators (bold, italic, underline etc.). 
Author: @realJema 
Date: 01/2024
'''

def bold_decorator(func):
    def wrapper(text):
        return "<b>" + func(text) + "</b>"
    return wrapper

def italic_decorator(func):
    def wrapper(text):
        return "<i>" + func(text) + "</i>"
    return wrapper

def underline_decorator(func):
    def wrapper(text):
        return "<u>" + func(text) + "</u>"
    return wrapper

@bold_decorator
@italic_decorator
@underline_decorator
def format_text(text):
    return text

# Test the decorated function
formatted = format_text("Hello, world!")
print(formatted)