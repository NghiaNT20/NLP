'''Write a Python program that takes a document as input and outputs a a lít ò the named entities in the document.
input: "Barack Obama was born in Hawaii. Kawha is a capital in Canada" 
this requires using a named entity recognition library like spacy
  '''

# # Take the input from the user
# document = "Barack Obama was born in Hawaii. Kawha is a capital in Canada"
# # Split the document into words
# words = document.split()
# # Initialize the list
# named_entities = []
# # Loop through the words
# for word in words:
#     # Check if the word is capitalized
#     if word.istitle():
#         # Add the word to the list
#         named_entities.append(word)
# # Print the list of named entities
# print("List of named entities:", named_entities)

import spacy
nlp = spacy.load("en_core_web_sm")
document = "Barack Obama was born in Hawaii. Kawha is a capital in Canada"
doc = nlp(document)
named_entities = [ent.text for ent in doc.ents]
print("List of named entities:", named_entities)
