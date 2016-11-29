# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.
def dasherize_number(num):
	num_string = str(num)
	new_num_string = ""
	for number in num_string:
		if int(number)%2 != 0:
			number = "-" + number + "-"
		new_num_string = new_num_string + number
	if new_num_string[0] == "-":
		new_num_string = new_num_string[1:]
	if new_num_string[-1] == "-":
		new_num_string = new_num_string[:(len(new_num_string) -1)]
	i = 1 
	while i < (len(new_num_string)-1):

		if (new_num_string[i] == "-" and new_num_string[i +1] == "-"):
			new_num_string = new_num_string[0: i] + new_num_string[i+1:]

		i +=1
	
	return new_num_string



print(
  'dasherize_number(303) == "3-0-3": ' +
  str(dasherize_number(303) == '3-0-3')
)
print(
  'dasherize_number(333) == "3-3-3": ' +
  str(dasherize_number(333) == '3-3-3')
)
print(
  'dasherize_number(3223) == "3-22-3": ' +
  str(dasherize_number(3223) == '3-22-3')
)