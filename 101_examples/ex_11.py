# How to lemmatize a given text ?
'''input:
text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."

output:
ext= 'dancing be an art . student should be teach dance as a subject in school . -PRON- dance in many of -PRON- school function . some people be always hesitate to dance .'

'''

# Lemmatization using spacy's lemma_ attribute of token

import spacy
nlp= spacy.load('en_core_web_sm')
text= "Dancing is an art. Students should be taught dance as a subject in schools . I danced in many of my school function. Some people are always hesitating to dance."

doc = nlp(text)
lemmatized = [token.lemma_ for token in doc]
" ".join(lemmatized)
print(" ".join(lemmatized))