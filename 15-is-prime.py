# Write a method that takes in an integer (greater than one) and
# returns true if it is prime; otherwise return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
# More generally, if `m` and `n` are integers, `m % n == 0` if and only
# if `n` divides `m` evenly.
#
# You would not be expected to already know about modulo for the
# challenge.
#
# Difficulty: medium.

def is_prime(num):
	if (num == 2 or num == 3):
		return True
	if num > 2:
		if num%2 == 0:
			return False
		if num%2 != 0:
			i = 3
			while i < num:
				if num%i == 0:
					return False
				i +=1
		else:
			return True
	else:
		return False


print('is_prime(2) == true: ' + str(is_prime(2) == True))
print('is_prime(3) == true: ' + str(is_prime(3) == True))
print('is_prime(4) == false: ' + str(is_prime(4) == False))
print('is_prime(9) == false: ' + str(is_prime(9) == False))