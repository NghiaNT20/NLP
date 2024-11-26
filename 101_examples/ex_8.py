# How to add custom stop words in spaCy ?
'''Add the custom stopwords “NIL” and “JUNK” in spaCy and remove the stopwords in below text


Input :

text=" Jonas was a JUNK great guy NIL Adam was evil NIL Martha JUNK was more of a fool "
Expected Output : 'Jonas great guy Adam evil Martha fool'

'''
import spacy
nlp=spacy.load('en_core_web_sm')

# Add custom stop words
text= " Jonas was a JUNK great guy NIL Adam was evil NIL Martha JUNK was more of a fool "
customize_stopwords = ['NIL', 'JUNK']

for w in customize_stopwords:
    nlp.vocab[w].is_stop = True
doc = nlp(text)
tokens = [token.text for token in doc if not token.is_stop]

' '.join(tokens)
print(' '.join(tokens))