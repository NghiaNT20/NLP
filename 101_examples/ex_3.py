#Print the tokens of the given text document
#Tokenization ưith nltk
# import nltk
# tokens= nltk.word_tokenize("Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided.")
# for token in tokens:

#     print(token)
#Tokenization with spacy
import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp("Last week, the University of Cambridge shared its own research that shows if everyone wears a mask outside home,dreaded ‘second wave’ of the pandemic can be avoided.")
for token in doc:
    print(token.text)   