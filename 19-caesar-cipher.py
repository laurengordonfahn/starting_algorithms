# Write a method that takes in an integer `offset` and a string.
# Produce a new string, where each letter is shifted by `offset`. You
# may assume that the string contains only lowercase letters and
# spaces.
#
# When shifting "z" by three letters, wrap around to the front of the
# alphabet to produce the letter "c".
#
# You'll want to use String's `ord` method and Integer's `chr` method.
# `ord` converts a letter to an ASCII number code. `chr` converts an
# ASCII number code to a letter.
#
# You may look at the ASCII printable characters chart:
#
#     http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters
#
# Notice that the letter 'a' has code 97, 'b' has code 98, etc., up to
# 'z' having code 122.
#
# You may also want to use the `%` modulo operation to handle wrapping
# of "z" to the front of the alphabet.
#
# Difficulty: hard. Because this problem relies on outside
# information, we would not give it to you on the timed challenge. :-)
def caesar_cipher(x, string):
    new_string = ""
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ind = 0
    swap = 0
    for letter in string:
        if letter not in alph:
            new_string = new_string + letter
        else:
            ind = alph.index(letter)
            if (ind + x) <= 25:
                new_string = new_string + alph[ind + x]
            else:
                swap = (ind + x) - 26
                new_string = new_string + alph[swap]
    print new_string
    return new_string



print(
  'caesar_cipher(3, "abc") == "def": ' +
  str(caesar_cipher(3, 'abc') == 'def')
)
print(
  'caesar_cipher(3, "abc xyz") == "def abc": ' +
  str(caesar_cipher(3, 'abc xyz') == 'def abc')
)