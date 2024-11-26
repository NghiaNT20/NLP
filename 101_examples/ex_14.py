# How to do spell correction in a given text ?
'''
Correct the spelling errors in the following text

Input :

text="He is a gret person. He beleives in bod"
Desired Output:

text="He is a great person. He believes in god"
'''
import textblob
from textblob import TextBlob

text = "He is a gret person. He beleives in bod"
text = TextBlob(text)
print (text.correct())
