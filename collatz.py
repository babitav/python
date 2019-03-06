# Babita, 2019-02-28
# Collatz.py 
# Program to perform calculations by taking current value 
# If even, divide by two
# If odd, multiply by three and add one
# program ends when current value is one 

currval = int(input("Please enter a positive number"))

# Check if the input number is not a positive integer(less than 1), ask user to enter the number again
while True:
  if currval <=0 : 
      currval = int(input("Please enter a positive number"))
  else:
    break

while currval >= 1:
    print (currval)

    if currval==1:
        break
    
    # Check if current val is even number, divide by two
    if currval %2 == 0:
        currval = int(currval/2)
        #print("even")
    else:
        currval = (currval * 3) + 1
        #print("odd")
         
    