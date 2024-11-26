'''Write a program to find all words that occur at least three times in the Brown Corpus.'''
from nltk.corpus import brown
from collections import Counter
words = brown.words()
word_freq = Counter(words)
for word, freq in word_freq.items():
    if freq >= 3:
        print(word)
        