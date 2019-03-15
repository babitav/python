# Babita, 2019-03-06
# Program to display today's date in given format
# Solution to problem 8 in Problem set 2019 

import datetime as dt

# Get today's date
x =dt.datetime.now() 

# prints today's date and time in the format specified in problem 8
# Day Month Date Year at Hour:Minute AM/PM
print(x.strftime("%A, %B %dth %Y at %I:%M%p"))

 
