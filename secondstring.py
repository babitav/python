# Babita 10-Mar-19
# Program to split the input string and print every second word

# Gt the input string
mystr = str(input("Please enter a sentence: "))

# Secondstring initialized
secondstr = ''

# Counter to check the position of words in string
ctr = 0

for i in mystr.split() :
    # i holds each word of the string 

    # If the position of word is even (0,2,4, etc.), i.e we take every alternate word
    # and add to the secondstr variable 
    if ctr %2 == 0 :
        secondstr = secondstr + i + ' '
    ctr= ctr +1

print (secondstr)