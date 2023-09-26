# Write a function to detect 13th Friday. 
# The function can accept two parameters, and both will be numbers. 
# The first parameter will be the number indicating the month, and the second will be the year in four digits. 
# Your function should parse the parameters, and it must return True when the month contains a Friday with the 13th, else return False.

import datetime
import calendar

def detect_Friday_13(year,month):
    #Get the thirteen day of the month
    day_13_of_the_month = datetime.date(year,month,13)
    print("The thirteenth day of month {} and year {} is a {}.".format(month,year,day_13_of_the_month.strftime("%A"))) 
    if day_13_of_the_month.weekday() == 4:
       print( True)
    else:
        print (False)

detect_Friday_13(year=2023,month=3)
detect_Friday_13(year=2024,month=12)
