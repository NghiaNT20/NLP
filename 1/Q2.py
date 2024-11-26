'''Find all the four-letter words in the Chat Corpus (text5). With the help ò a frequency distribution (FreqDist), show these words in decreasing order of frequency.'''
from nltk.book import text5
from nltk import FreqDist
words = text5
new_words = []
for word in words:
    if len(word) == 4:
        new_words.append(word)
fdist = FreqDist(new_words)
print(fdist.most_common())
