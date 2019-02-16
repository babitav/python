# Ian McLoughlin, 2018-02-01
# Is it Tuesday?

import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yay! It is Tuesday.")
else:
  print("Unfortunately it is not Tuesday.")
print(datetime.today().weekday());
