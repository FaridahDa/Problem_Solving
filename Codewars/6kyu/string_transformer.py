"""
Given a string, return a new string that has transformed based on the input:

Change case of every character, ie. lower case to upper case, upper case to lower case.
Reverse the order of words from the input.
Note: You will have to handle multiple spaces, and leading/trailing spaces.

For example:

"Example Input" ==> "iNPUT eXAMPLE"
You may assume the input only contain English alphabet and spaces.
"""

def string_transformer(s):
    # return a transformed string from the input
    # change case of characters.. eg lower to upper or upper to lower
    # reverse the order of the input
    # have to handle spaces and leading/trailing spaces

    words = s.split(' ')
    reversed_words = ' '.join(reversed(words))
    return reversed_words.swapcase()
