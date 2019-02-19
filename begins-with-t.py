# Babita, 2010-02-19
# Program to check if the current day starts with letter'T'

import datetime

# Get today's date
x =datetime.datetime.today() 

# Check the weekday number, 0 is Sunday, 
# so Tuesday and Thursday (beginning wit T) are 2 and 4
# if weekday is 2 or 4, print yes it starts wit T else no
if (x.strftime("%w") == '2') or (x.strftime("%w") == '4')  :
  print("Yes - Today begins with 'T'")
else:
  print("No - Today doesn't begin with 'T'")
