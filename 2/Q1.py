''' Define s as a text
write expressions for finding all words in s that ending in "ize"
The result should be a list of words: ['word1', 'word2', ...]'''

import re

text = "The ghostize that says booize haunts the loo"
words = text.split()
new_word = []

for word in words:
    if re.search("ize$", word):
        new_word.append(word)

print(new_word)