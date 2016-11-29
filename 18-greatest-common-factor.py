# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.
#
# Difficulty: medium.

def greatest_common_factor(x, y):
    lowest = None
    if x < y:
        lowest = x
    else:
        lowest = y
    
    factor = None
  
    for num in range(1, (lowest+1)):
        if (x%num == 0 and y%num == 0):
            factor = num
 
    return factor



print(
  'greatest_common_factor(3, 9) == 3: ' +
  str(greatest_common_factor(3, 9) == 3)
)
print(
  'greatest_common_factor(16, 24) == 8: ' +
  str(greatest_common_factor(16, 24) == 8)
)
print(
  'greatest_common_factor(3, 5) == 1: ' +
  str(greatest_common_factor(3, 5) == 1)
)