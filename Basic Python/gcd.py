'''
Name: Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
Author: @realJema 
Date: 04/2024
'''


import math 

# Method 1 
a = int(input("Enter a: "))
b = int(input("Enter b: "))

ans = math.gcd(a, b) 
print(ans) 

# Method 2 

min_ab = min(a, b)
y = a * b 

gcd = 0 
for i in range(1, min_ab + 1): 
    if(a % i == 0) & (b % i == 0):
        if i > gcd: 
            gcd = i 

print(gcd)
