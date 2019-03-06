# Babita, 2019-03-01
# prime.py 
# Solution to problem 5 in Problem set 2019 
# Program to check if the input number is prime or not
# A prime number has two factors itself, 1 and the no. itself
# so we will check if the given number has any other factor/multiple
# then it is not a prime

i = 0

chkprime  = int(input("Please enter a positive number"))

# Check if the input number is not a positive integer(less than 1), ask user to enter the number again
while True:
  if chkprime <=0 : 
      chkprime = int(input("Please enter a positive number"))
  else:
    break

# Check if the given number has any other factor apart from 1 and the number itself
# Start checking from 2 till the number itself
for i in range (2,chkprime+1):

    # If any number is a factor, the remainder will be zero, 
    # so the number is not prime, we break from for and dont chk any other factors
    if (chkprime%i == 0):
        break

# After the For loop, chk if i has traversed all the numbers till the given input number
# If yes, it means it couldnt find any other factor of the given number (apart from the number itself )
# so it is prime,
# If i is less than chkprime, means it has not traversed the entire for loop, 
# it means chkprime has some other factors (apart from the number itself)  
# which were found in for loop, leading to exit from for loop
if (i == chkprime):
    print ("The number is prime")   
else :
    print ("The number is not prime")   
