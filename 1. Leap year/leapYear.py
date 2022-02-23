"""This program ask to a user to write a year and check if that 
year is a leap year or not.
it is one of the first exercises of the Python course of the 
online plateform OpenClassrooms.com
Skills check : conditions in Python
@Author : tizianoadv
"""

import os #Import the OS module to make a pause at the end of the program

print("Leap year")
year = input("Choose a year : ")
year = int (year)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0 ):
    print("It's a leap year !\n")
else :  
    print("It's not a leap year !\n")
    
os.system("pause")