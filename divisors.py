# Babita 20-Feb-19
# Solution to problem 3 in Problem set 2019 

#Loop from numbers 1000 to 10000
for i in range(1000,10001):

	#Check if the number is divisible by 6 (means the remainder after dividing by 6 is zero)
	if i%6 == 0:

		# Here the number is divisible by 6, we further need to check if the number is divisible by 12
		# If number is not divisible by 12, the remainder should be greater than zero which is
		# being checked in condition below     
		if i%12 != 0: 
			
			#This means the number is not divisible by 12
			# So it is concluded that the number is divisible by 6 and not by 12
			print(i)
