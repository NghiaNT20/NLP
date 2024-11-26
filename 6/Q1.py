'''Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in ascending order of frequency.'''
import nltk
from nltk.corpus import nps_chat
from nltk.probability import FreqDist

# Load the chat corpus (text5)
text5 = nps_chat.words()

# Filter for four-letter words
four_letter_words = [word.lower() for word in text5 if len(word) == 4]

# Calculate the frequency distribution of four-letter words
fdist = FreqDist(four_letter_words)

# Display the words in ascending order of frequency
for word, frequency in sorted(fdist.items(), key=lambda item: item[1]):
    print(f'{word}: {frequency}')

