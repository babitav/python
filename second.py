# Babita 15-Mar-19
# Solution to problem 9 in Problem set 2019 
# Program to read a text file and output every second line

# First input the file name of the file to be read 
file_to_read  = str(input("Please enter the file to be read: "))

i=0
try:
    with open(file_to_read) as f:
        #read_data = f.readline()
        for line in f:
            if i%2 == 0:
                print(line)
            i = i + 1

except OSError as err:
    print("OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
