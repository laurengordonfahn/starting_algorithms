# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# You'll want to use the `split` and `join` methods. Also, the String
# method `upcase`, which converts a string to all upper case will be
# helpful.
#
# Difficulty: medium.
def capitalize_words(string):
	new_string = string[0].upper() + string[1:]
	i = 1
	while i < (len(new_string) - 1):	
		if new_string[i] == " ":
			new_string = new_string[:i + 1] + new_string[i+1].upper() + new_string[i+2:]

		i +=1
	return new_string



print(
  'capitalize_words("this is a sentence") == "This Is A Sentence": ' +
  str(capitalize_words("this is a sentence") == "This Is A Sentence")
)
print(
  'capitalize_words("mike bloomfield") == "Mike Bloomfield": ' +
  str(capitalize_words("mike bloomfield") == "Mike Bloomfield")
)