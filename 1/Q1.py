'''Define s as a text
write expressions for finding all words in s that all uppercase first character.
the result should be in the form of a list of words:['word1', 'word2', 'word3', ...]'''

s = "This is a Sentence. This is anoTher Sentence. This is a Third Sentence."
words = s.split()
new_words = []
for word in words:
    if word[0].isupper():
        new_words.append(word)
print(new_words)