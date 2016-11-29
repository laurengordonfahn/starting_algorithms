# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.
#
# Difficulty: medium.

def scramble_string(string, array):
	diction = {}
	i = 0
	while i < len(string):
		diction[(array[i])] = string[i]
		i +=1
	
	j = 0 
	new_string = ""
	while j < len(string):
		new_string = new_string + diction[j]
		j +=1
	print new_string
	return new_string

# scramble_string("abcd", [3, 1, 2, 0])


print(
  'scramble_string("abcd", [3, 1, 2, 0]) == "dbca":'  +
  str(scramble_string("abcd", [3, 1, 2, 0]) == "dbca")
)
print(
  'scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vroakm"):'  +
  str(scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vroakm"))