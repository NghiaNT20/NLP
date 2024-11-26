'''Write a Python NLTK program to tokenize words, sentence wise.
Sample Output:
Original string:
Joe waited for the train. The train was late Mary and Samantha took the bus. I looked for
Mary and Samantha at the bus station.
Tokenize words sentence wise:
Read the list:
['Joe', waited', 'for',  'train', '.']
['The', 'train', 'was',  'late', '.']
['Mary', 'and', 'Samantha', 'took', 'the', 'bus', '.']
['I', 'looked', 'for', 'Mary', 'and', 'Samantha', 'at', 'the', 'bus', 'station', '.']''' 
import re

document = "Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."

pattern = r'\b\w+\b|[.]'
tokens = re.findall(pattern, document)
# print(tokens)
array = []
for token in tokens:
    if (token!= "."):
        array.append(token)
    else:
        array.append(token)
        print(array)
        array = []

        