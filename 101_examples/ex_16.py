# How to extract all the nouns in a text?
'''Extract and print all the nouns present in the below text

Input:

text="James works at Microsoft. She lives in manchester and likes to play the flute"
Desired Output :

James
Microsoft
manchester
flute
'''

import spacy
nlp = spacy.load('en_core_web_sm')

text="James works at Microsoft. She lives in manchester and likes to play the flute"

doc = nlp(text)
for token in doc:
    if token.pos_ == 'NOUN' or token.pos_ == 'PROPN':
     print(token.text)
