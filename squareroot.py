# Babita 20-Mar-19
# Program to calculate the square root of a given number 

try:
    getroot  = int(input("Please enter a positive number whose square root needs to be determined "))

    # Check if the input number is not a positive integer(less than 1), ask user to enter the number again
    while True:
        if getroot  <=0 : 
            getroot = int(input("Please enter a positive number "))
        else:
            break

    estimate = getroot / 2

    #Keep going until the square of estimate is within 0.1 of getroot
    while abs((estimate * estimate) -getroot) > 0.01:

        # This is Newton's method to improve the estimate
        # Adapted from https://tour.golang.org/flowcontrol/8
        estimate = ( (estimate * estimate) -getroot ) / (2 * estimate) 

    # Show the result i.e. square root of the number getroot
    print (f"The square root of {getroot} is approx. {abs(estimate)} ")

except ValueError:
    print ("Please enter a +ve number and not a string")
except TypeError:
    print ("Type Error - Please enter a +ve number and not a string")