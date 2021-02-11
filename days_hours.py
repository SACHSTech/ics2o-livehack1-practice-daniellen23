"""
Name: days_hours.py

Purpose: This program will convert user inputted amount of hours into days and hours.

Author: Nguyen.D 

Created: 2021-02-08
"""
hours = int(input("Enter amount of hours: "))
days = hours / 24
new_hours = hours % 24 
print("Number of days: ", (int(days)))
print("Number of hours: ", (int(new_hours)))