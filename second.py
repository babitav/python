# Babita 15-Mar-19
# Solution to problem 9 in Problem set 2019 
# Program to read a text file and output every second line

import sys

try:
    if len(sys.argv)!=2 :
    #   If the number of arguments < 2 or > 2, exit and display the proper message 
        sys.exit() 

    # Assign the file name to be read from the second system argument to the file_to_read variable
    file_to_read = sys.argv[1]

    #Print every second / Alternate line starting from line 1 
    i=0 # Ctr to track line number

    with open(file_to_read) as f:
        for line in f:
            if i%2 == 0: # If an even line, print the same.. this way alternate lines are only printed
                print(line)
            i = i + 1

except SystemExit:
    if len(sys.argv)==1 :
        print("You should supply a file name to be read")
    else:
        print("You should supply only one file name to be read")            
except OSError as err:
    print("OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
