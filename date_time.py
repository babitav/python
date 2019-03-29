# Babita, 2019-03-06
# Program to display today's date in given format
# Solution to problem 8 in Problem set 2019 

import datetime as dt

# Get today's date
x =dt.datetime.now() 

# prints today's date and time in the format specified in problem 8
# Day Month Date Year at Hour:Minute AM/PM

# Get the day number part of the date
day = x.strftime("%d")

# If day is 1, 21 or 31 - print 'st' after day number i.e. 1st, 21st , 31st
# If day is 2 or 22 - print 'nd' after day number i.e. 2nd, 22nd 
# If day is 3 or 23 - print 'rd' after day number i.e. 3rd, 23rd 
# Else print 'th' after day part like 7th, 15th, 28th etc.

if ((day == "01") or (day == "21") or (day== "31")):
    print(x.strftime("%A, %B %dst %Y at %I:%M%p"))
elif ((day == "02") or (day == "22")):
    print(x.strftime("%A, %B %dnd %Y at %I:%M%p"))
elif ((day == "03") or (day == "23")):
    print(x.strftime("%A, %B %drd %Y at %I:%M%p"))
else:
    print(x.strftime("%A, %B %dth %Y at %I:%M%p"))

 
