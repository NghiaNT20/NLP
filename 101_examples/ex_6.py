#  How to tokenize text with stopwords as delimiters?
'''Tokenize the given text with stop words (“is”,”the”,”was”) as delimiters. Tokenizing this way identifies meaningful phrases. Sometimes, useful for topic modeling

Input :

text = "Walter was feeling anxious. He was diagnosed today. He probably is the best person I know.""
Expected Output :['Walter',
 'feeling anxious',
 'He',
 'diagnosed today',
 'He probably',
 'best person I know']
'''


# Solution
text = "Walter was feeling anxious. He was diagnosed today. He probably is the best person I know."

stop_words_and_delims = ['was', 'is', 'the', '.', ',', '-', '!', '?']
for r in stop_words_and_delims:
    text = text.replace(r, 'DELIM')

words = [t.strip() for t in text.split('DELIM')]
words_filtered = list(filter(lambda a: a not in [''], words))
print(words_filtered)
