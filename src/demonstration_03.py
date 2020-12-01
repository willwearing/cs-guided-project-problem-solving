"""
Challenge #3:
​
Given a string of numbers separated by a comma and space, return the product of the numbers.
​
Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20
​
- 
​
Notes:
- Bonus: Try to complete this challenge in one line!
"""
import math
​
def multiply_nums(nums):
    '''
    Input: a single string of comma-separated numbers 
​
    Input: a list of numbers 
    Output: int that is the product of all the numbers in the string 
​
    This is a variant being asked to multiply a list of numbers     
    '''
    # let's turn the string into a list of nums
    # we need to take a string of comma-separated numbers and turn it
    # into a list of numbers 
    # split each string element by ', '
    split = nums.split(', ')
​
    # `split` now holds a list of string digits 
    # take each of those string digits and turn each of them into an int 
    ints = [] 
​
    for digit in split:
        ints.append(int(digit))
​
    return math.prod(ints)
​
    # return math.prod(int(digit) for digit in nums.split(', '))
​
print(multiply_nums("2, 3"))