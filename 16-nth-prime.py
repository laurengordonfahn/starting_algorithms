# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime.
#
# Difficulty: medium.

def nth_prime(num):
	prime_array = []
	i = 2
	while len(prime_array) < num:
		if len(prime_array) == 0:
			prime_array.append(2)
		else:
			j = 2
			k = None
			while j < i :
				if i%j != 0:
					k = i
					j +=1
				else:
					k = None
					break
			if k == i:
				prime_array.append(i)
		i +=1

	print prime_array
	return prime_array[num-1]





print('nth_prime(1) == 2: ' + str(nth_prime(1) == 2))
print('nth_prime(2) == 3: ' + str(nth_prime(2) == 3))
print('nth_prime(3) == 5: ' + str(nth_prime(3) == 5))
print('nth_prime(4) == 7: ' + str(nth_prime(4) == 7))
print('nth_prime(5) == 11: ' + str(nth_prime(5) == 11))
