"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""

def anagrams(word, words):
    #finding all the anagrams of a word from a list
    #2 inputs, a word and array with words
    # return an array of all the anagrams or an empty anagram if none
    # get word, sort it, get the array sort it, compared word with array..
    #if its the same then append to empty array, then return that array
    #your code here
    new_word = sorted(word)
    new_array = []
    result = []
#     for anag in words:
#         new_array.append(sorted(anag))

    for i in words:
        if sorted(i) == new_word:
            result.append(''.join(i))
    return result
