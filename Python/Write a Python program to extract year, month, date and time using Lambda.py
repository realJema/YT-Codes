'''
Name: Write a Python program to extract year, month, date and time using Lambda. 
Author: @realJema 
Date: 01/2024
'''

import datetime 

date_time = datetime.datetime.now() 

year = lambda dt: dt.year 
month = lambda dt: dt.month 
day = lambda dt: dt.day 
time = lambda dt: dt.time() 

print(f"The year is {year(date_time)}")
print(f"The month is {month(date_time)}")
print(f"The day is {day(date_time)}")
print(f"The time is {time(date_time)}")