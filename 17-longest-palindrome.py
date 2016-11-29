# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# You may want to use Array's `slice(start_index, length)` method,
# which returns a substring of length `length` starting at index
# `start_index`:
#
#     "abcd".slice(1, 2) == "bc"
#     "abcd".slice(1, 3) == "bcd"
#     "abcd".slice(2, 1) == "c"
#     "abcd".slice(2, 2) == "cd"
#
# Difficulty: hard.
# def cleaner(string):
#     for ind, letter in enumerate(string):
#         if letter != letter.lower()
#             print "String must not contain any uppercase letters."
      
#         if letter == string[ind+1]:
#             print "String must not contain consectuive repeat letters"

            
def palindrome(string):
  i = 0
  inverti = (len(string) - 1)
  
  while i < len(string):
	 	if string[i] != string[inverti - i]:
	 		return False
	 	i +=1
  return True
# Test Palindrome = pass
# print(palindrome("abba"))
# print(palindrome("ab"))


def longest_palindrome(string):
  longest = ""
    # cleaner(string)
    

  if palindrome(string) == True:
    if len(string) > len(longest):
      longest = string 
    return longest
    
    
  i = 0

  while i < len(string):
    j = 0

  
   
    
    while j  < len(string):
      end = (len(string) - j)
      new_string =  string[i : end]
      
      if palindrome(new_string) == True:
        if len(new_string) > len(longest):
          print i
          print j
          print longest
          longest = new_string
         
      j +=1
    i +=1
  print longest
  return longest


print(
  'longest_palindrome("abcbd") == "bcb": ' +
  str(longest_palindrome('abcbd') == 'bcb')
)
print(
  'longest_palindrome("abba") == "abba": ' +
  str(longest_palindrome('abba') == 'abba')
)
print(
  'longest_palindrome("abcbdeffe") == "effe": ' +
  str(longest_palindrome('abcbdeffe') == 'effe')
)