"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    """
    Input: string of all lowercase letters and/or spaces
    Output: int representing the number of vowels in our input string

     keep a counter 
     iterate through our input string and check to see if the current letter
     is a vowel
     if it is, increment our counter
    """

    vowels = "aeiou"
    
    counter = 0

    for letter in input_str.lower():
        if letter in vowels:
            counter += 1
    return counter

print(get_count('Harry Potter and the Order of the Phoenix'))


