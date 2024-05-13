'''
Name: Calculate income tax for the given income by adhering to the rules below
Rate 
Fist 10,000     --- 0
Next 10,000     --- 10
Remaining       --- 20 

Author: @realJema 
Date: 04/2024
'''

income = 45000 
tax_payable = 0 
print("Gien income: ", income)

if income <= 10000:
    tax_payable = 0 
elif income <= 20000:
    x = income - 10000 # no tax on first 10,000
    tax_payable = x * 10 / 100 
else: 
    tax_payable = 0 
    tax_payable = 10000 * 10 / 100 
    tax_payable += (income - 20000) * 20 / 100 

print("Total tax to pay is ", tax_payable)
