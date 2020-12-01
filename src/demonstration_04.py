"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :(

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    """
    Inputs: String that represents a sentences (it always starts with make me)
    Output: String with the emote word replaced with an emoticon
    """

    #if we're using conditionals
    # assuming every input sentence is 3 words
    #do an if check on the last word in the sentence
    words = txt.split(' ')
    last_word = words[-1]

    #check if the last word is one of the words we care about
    #if we see it, replace the word with the corresponding emoticon

    # if last_word == "smile":
    #     words[-1] = ':D'
    # if last_word == "grin":
    #     words[-1] = ":)"
    # if last_word == "sad":
    #     words[-1] = ':('
    # if last_word == "mad":
    #     words[-1] = ":("

    # we're using these if statements to represent associations between
    # certain words and their emoticons
    # what's another way to represent associations in code?
    # dictionaires represent associations in the form of key value pairs

    associations = {
        "smile": ':)',
        "mad": ">:(",
        "grin": ":)",
        "sad": ":("
    }

    # turn the last word in the words list into it's corresponding emoticon
    # by using it as a key to fetch its value in our dictionary
    words[-1] = associations[last_word]

    return ' '.join(words)

print(emotify('make me mad'))