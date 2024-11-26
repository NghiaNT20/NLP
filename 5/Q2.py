'''Define a function percent(word, text) that calculates how often a given word occurs in a text
and expresses the result as a percentage.'''
import re
def percent(word, text):
    words = re.findall(r'\b\w+\b', text)
    return round(words.count(word) / len(words) * 100, 2)
s = "The script was written by a script writer"
print(percent('script', s))
print(percent('writer', s))