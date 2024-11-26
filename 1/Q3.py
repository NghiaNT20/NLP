'''Write a Python NLTK program to create a list of words from a given string '''


import nltk
from nltk import word_tokenize
text = " Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."
words = word_tokenize(text)
print(words)
