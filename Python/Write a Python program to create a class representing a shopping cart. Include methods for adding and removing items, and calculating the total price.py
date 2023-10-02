'''
Name: Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price
Author: @realJema 
Date: 09/2023
'''

class ShoppingCart: 
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items: 
            self.items[item] += price 
        else: 
            self.items[item] = price 

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else: 
            print(f"{item} is not in the shopping cart.")

    def calculate_total_price(self): 
        total_price = sum(self.items.values())
        return total_price 
    
# Usage 
my_cart = ShoppingCart() 

my_cart.add_item("Apple" , 1.50)
my_cart.add_item("Banana", 0.75)
my_cart.add_item("Apple" ,1.50)  # duplicate item 

print("Total price:", my_cart.calculate_total_price())

my_cart.remove_item("Banana")
my_cart.remove_item("Orange") # removing item that is not present 

print("Total price: ", my_cart.calculate_total_price())