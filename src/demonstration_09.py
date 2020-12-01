"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    """
    Input: string of odd or even length
    Output: a single letter if the input string is odd length, two letters if the
            input is even length
    
    First, need to figure out if our word is odd or even length
    Depending on which case we're looking at, we need to do things 
    slightly differently

    For both cases, we're going to need to find the middle index

    If input is odd
        return the character at the middle index

    If input is even
        return the character at the middle index (floored) plus the character right after
    """
    midpoint = (len(input_str) - 1) // 2

    #even case
    if len(input_str) % 2 == 0:
        #return the letter at the midpoint + the letter after it
        return input_str[midpoint : midpoint + 2]
    #odd case
    return input_str[midpoint]

print(get_middle('testing')) 

