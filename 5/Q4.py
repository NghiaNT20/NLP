'''Extract the Verb Phrases from the given text
input:
text = " I may bake a cake for my birthday. The talk will introduce reader about Use of banking"
Desired Ouput: 
            may bake
            will introduce'''
import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

# Sample text
text = "I may bake a cake for my birthday. The talk will introduce readers about the use of banking."

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(tokens)

# Define the chunk grammar for verb phrases
grammar = r"""
  VP: {<MD>?<VB|VBD|VBG|VBN|VBP|VBZ><RB|RP|JJ|NN|IN>*}
"""
# # Define the chunk grammar for noun phrases
# grammar = r"""
#   NP: {<DT|PP\$>?<JJ>*<NN|NNS|NNP|NNPS>+}
#       {<NNP>+}
# """

# # Define the chunk grammar for adjective phrases
# grammar = r"""
#   AP: {<RB|RBR|RBS>*<JJ>}
# """

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the tagged words
tree = chunk_parser.parse(pos_tags)

# Extract and print the verb phrases
verb_phrases = []
for subtree in tree.subtrees(filter=lambda t: t.label() == 'VP'):
    verb_phrase = " ".join(word for word, tag in subtree.leaves())
    verb_phrases.append(verb_phrase)

# Display the result
for vp in verb_phrases:
    print(vp)