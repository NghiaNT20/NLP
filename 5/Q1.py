'''Define s as a text
Write expressions for finding all words in s that contain the sequence of letters pt
The result should be in the form of a list of words: ['word1', 'word2,.J.'''
import re
s = "The script was written by a script writer"
print(re.findall(r'\b\w*pt\w*\b', s))


