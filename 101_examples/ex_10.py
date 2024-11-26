# How to perform stemming?
''' Perform stemming/ convert each token to it’s root form in the given text


Input :

text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."
Desired Output:

text= 'danc is an art . student should be taught danc as a subject in school . I danc in mani of my school function . some peopl are alway hesit to danc .'
'''
# Stemming with nltk's PorterStemmer

import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."

stemmed_tokens=[]

for token in nltk.word_tokenize(text):
    stemmed_tokens.append(stemmer.stem(token))

" ".join(stemmed_tokens)
print(" ".join(stemmed_tokens))
