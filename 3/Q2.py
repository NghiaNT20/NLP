'''write a function that takes a text and vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary. both arguments can be represented as lists of strings.'''
def words_not_in_vocab(text, vocabulary):
    vocab_set = set(vocabulary)
    
    words_in_text = set(text)
    
    return words_in_text - vocab_set

text = ['the', 'cat', 'sat', 'on', 'the', 'mat']
vocabulary = ['the', 'cat', 'on', 'sat']
result = words_not_in_vocab(text, vocabulary)
print(words_not_in_vocab(text, vocabulary)) 
