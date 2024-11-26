'''Find the similarity between any two words.

Input :

word1="amazing"
word2="terrible"
word3="excellent"
Desired Output:

#> similarity between amazing and terrible is 0.46189071343764604
#> similarity between amazing and excellent is 0.6388207086737778'''

# import spacy

# # Load the medium-sized English language model with word vectors
# nlp = spacy.load("en_core_web_md")

# def calculate_similarity(word1, word2):
#     # Create spaCy tokens for the words
#     token1 = nlp(word1)
#     token2 = nlp(word2)
    
#     # Calculate and return the similarity between the two words
#     return token1.similarity(token2)

# # Words to compare
# word1 = "amazing"
# word2 = "terrible"
# word3 = "excellent"

# # Calculate and print the similarities
# similarity_1 = calculate_similarity(word1, word2)
# similarity_2 = calculate_similarity(word1, word3)

# print(f"Similarity between {word1} and {word2} is {similarity_1}")
# print(f"Similarity between {word1} and {word3} is {similarity_2}")

import spacy

nlp=spacy.load('en_core_web_lg')

word1="amazing"
word2="terrible"
word3="excellent"

token1=nlp(word1)
token2=nlp(word2)
token3=nlp(word3)

# Use similarity() function of tokens
print('similarity between', word1,'and' ,word2, 'is' ,token1.similarity(token2))
print('similarity between', word1,'and' ,word3, 'is' ,token1.similarity(token3))