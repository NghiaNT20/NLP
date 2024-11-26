# How to remove punctuations ?
''' Remove all the punctuations in the given text
Input :

text="The match has concluded !!! India has won the match . Will we fin the finals too ? !"

Desired Output :

'The match has concluded India has won the match Will we fin the finals too'
'''

# Removing punctuations in spaCy
# import spacy
# nlp= spacy.load('en_core_web_sm')

# text="The match has concluded !!! India has won the match . Will we fin the finals too ? !"
# doc = nlp(text)
# new_tokens = []
# for token in doc:
#     if token.is_punct==False:
#         new_tokens.append(token.text)
# ' '.join(new_tokens)

# print(' '.join(new_tokens))

# Removing punctuation in nltk with RegexpTokenizer
import nltk

from nltk.tokenize import RegexpTokenizer

text="The match has concluded !!! India has won the match . Will we fin the finals too ? !"

tokenizer=nltk.RegexpTokenizer(r"\w+")

tokens=tokenizer.tokenize(text)


" ".join(tokens)
print(" ".join(tokens))