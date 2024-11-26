'''Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.'''
import nltk
from nltk import word_tokenize

def percent(word, text):
    words = word_tokenize(text)
    word_count = words.count(word)
    total_words = len(words)
    word_percent = (word_count / total_words) * 100
    return word_percent

text = input("Enter a text: ")
word = input("Enter a word: ")
result = percent(word, text)
print(f"The word '{word}' occurs in the text {result:.2f}% of the time.")
