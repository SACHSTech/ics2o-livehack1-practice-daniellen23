""""
Name: f_to_c.py

Purpose: This program will convert the user inputted fahrenheit degree and print into celsius. 

Author: Nguyen.D

Created: 2021-02-08
"""
#c=5/9(f-32)
language = "python3"
fahrenheit = int(input("Enter Fahrenheit: "))
celsius = (fahrenheit - 31) * (5 / 9)
print(fahrenheit, "degrees fahrenheit converted to celsius: ", int(celsius), "degrees")