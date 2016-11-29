# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.
#
# Difficulty: hard.

def num_repeats(string):
    hash_letter = {}
    letter_array = []
    
    for letter in string:
        if hash_letter.get(letter, None) == None:
            hash_letter[letter] =  1
        else: 
            count = hash_letter[letter]
            hash_letter[letter] = count + 1
    for letter in hash_letter:
        if hash_letter[letter] > 1:
            letter_array.append(letter)

    # print letter_array
    # print hash_letter
    # print len(letter_array)
    return len(letter_array)






print('num_repeats("abdbc") == 1: ' + str(num_repeats('abdbc') == 1))
# one character is repeated
print('num_repeats("aaa") == 1: ' + str(num_repeats('aaa') == 1))
print('num_repeats("abab") == 2: ' + str(num_repeats('abab') == 2))
print('num_repeats("cadac") == 2: ' + str(num_repeats('cadac') == 2))
print('num_repeats("abcde") == 0: ' + str(num_repeats('abcde') == 0))