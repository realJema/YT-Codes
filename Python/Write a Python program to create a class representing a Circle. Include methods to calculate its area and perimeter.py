'''
Name: Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
Author: @realJema 
Date: 09/2023
'''

import math 

class Circle: 
    def __init__(self, radius):
        self.radius = radius 

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self): 
        return 2 * math.pi * self.radius 
    

# Example 
circle = Circle(15) # sets the radius to 5
print("Area:", circle.calculate_area())
print("Perimeter:", circle.calculate_perimeter())