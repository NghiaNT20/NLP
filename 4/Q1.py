'''Define s as a text
Write expressions for finding all words in s that contain the letter z.
The result should be in the form of a list of words: ['wordi" word2, ...1.'''
s = 'the quick brown fox jumps over the lazy dog'
words = s.split()
for word in words:
    if 'z' in word:
        print(word)
