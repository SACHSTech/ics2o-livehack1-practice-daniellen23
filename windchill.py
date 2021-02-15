""""
Name: windchill.py

Purpose: This program will convert the wind chill valued using the user inputted temperature, in celsius, and the wind speed.

Author: Nguyen.D

Created: 2021-02-11
"""
import math
#wind_chill=13.12+(0.6215XT)-11.37 x V0.16) + (0.3965 x T x V0.16)
celsius = int(input("Enter Temperature in Celsius: "))
wind_speed = int(input("Enter Wind Speed in km/hr: "))

wind_chill = 13.12 + (0.6215 * celsius) -  11.37 * math.pow(wind_speed, 0.16) + (0.3965 * celsius * math.pow(wind_speed, 0.16))

print("Wind chill is:  ", int(wind_chill))