# Babita, 2019-03-06
# Program to display today's date in given format
# Solution to problem 8 in Problem set 2019 

import datetime

# Get today's date
x =datetime.datetime.now() 

print(x.strftime("%A", "%B"))

#, "%d", "th ", "%Y", " at ", "%I",":", "%M"","%p" 
