"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
solution("camelCasing")  ==  "camel Casing"
"""



def solution(s):
    # break word up
    # put whitspace before capital letter
    new_s = ''
    for letter in s:
        if letter.isupper():
            new_s += ' ' + letter

        else:
            new_s += letter
    return new_s