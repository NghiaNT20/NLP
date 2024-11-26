'''Write a Python NLTK program to split the text sentence/paragraph into a list of words.
Sample Output:
Original string:
Joe
waited for the train. The train was late. Mary and Samantha took the bus. I looked for
Mary and Samantha at the bus station.
Sentence-tokenized copy in a list:
['Joe waited for the train.', 'The train was late.', 'Mary and Samantha took the bus.', 'I looked for Mary and Samantha at the bus station.']
Read the list:
Joe waited for the train.
The tratn was late.
Mary and Samantha took the bus.
I looked for Mary and Samantha at the bus station.'''
from nltk.tokenize import sent_tokenize
text = '''Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station.'''
print("Original string:")
print(text)
print("\nSentence-tokenized copy in a list:")
print(sent_tokenize(text))
print("\nRead the list:")
for s in sent_tokenize(text):
    print(s)