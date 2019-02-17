# Babita, 2019-01-30
# Sum of numbers from 1 to the input number 

sum = 0
i = 1
sumupto = int(input("Please enter a positive number"))

# Check if the input number is not a positive integer(less than 1), ask user to enter the number again
while True:
  if sumupto <=0 : 
      sumupto = int(input("Please enter a positive number"))
  else:
    break

# Loop from 1 till the input number and add the number i to the sum
while i <= sumupto :
  sum = sum + i
  i = i + 1

print ("The sum of numbers from 1 to",sumupto, "is ", sum)

