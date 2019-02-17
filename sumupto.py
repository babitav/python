# Babita, 2019-01-30
# Sum of numbers from 1 to the input number 

sum = 0
i = 1
sumupto = int(input("Please enter a positive number less than 10 "))

while True:
  if sumupto >10 :
    sumupto = int(input("Please enter a positive number less than 10 "))
  elif sumupto <=0 : 
      sumupto = int(input("Please enter a positive number less than 10 "))
  else:
    break

while i <= sumupto :
  sum = sum + i
  i = i + 1

print ("The sum of numbers is", sum)

