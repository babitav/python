# Babita, 2019-02-28
# Collatz.py 
# Program to perform calculations by taking current value 
# If even, divide by two
# If odd, multiply by three and add one
# program ends when current value is one 

try:
    currval = int(input("Please enter a positive number "))

    # Check if the input number is not a positive integer(less than 1), ask user to enter the number again
    while True:
        if currval <=0 : 
            currval = int(input("Please enter a positive number "))
        else:
            break

    # Keep looping as long as value > 1
    while currval >= 1:
        print (currval)

        # If value is 1, break from the loop and exit from the program 
        if currval==1:
            break
    
        # Check if current val is even number, divide by two
        if currval %2 == 0:
            currval = int(currval/2)
        else:
            currval = (currval * 3) + 1
         
except ValueError:
    print ("Please enter a +ve number and not a string")
except TypeError:
    print ("Type Error - Please enter a +ve number and not a string")