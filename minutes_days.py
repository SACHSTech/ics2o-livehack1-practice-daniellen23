"""
Name: minutes_days.py

Purpose: This program will convert user inputted amount of minutes into days, hours and minutes.

Author: Nguyen.D 

Created: 2021-02-11
"""
minutes = int(input("Enter amount of minutes: "))
days = minutes / 1440
#days = 1440 minutes
#hours = 60 minutes
remaining_hours = minutes % 1440
new_hours = remaining_hours / 60
new_minutes = minutes % 60

print("Number of days: ", (int(days)))
print("Number of hours: ", (int(new_hours)))
print("Number of minutes: ", (int(new_minutes)))
