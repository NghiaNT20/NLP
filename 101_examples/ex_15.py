# How to tokenize tweets ?
'''Clean the following tweet and tokenize them

Input :

text=" Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "
Desired Output :

['Having',
 'lots',
 'of',
 'fun',
 'goa',
 'vaction',
 'summervacation',
 'Fancy',
 'dinner',
 'Beachbay',
 'restro']
 ```'''  

import re
text=" Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro :) "

text = re.sub(r'[^\w]', ' ', text)

from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer()
tokenizer.tokenize(text)
print(tokenizer.tokenize(text))