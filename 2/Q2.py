'''Write a function that finds the 50 most frequency occurring words of a text that are not stopwords. '''
import nltk
from collections import Counter
from nltk.corpus import stopwords
import string

# Make sure to download the stopwords corpus if you haven't already
# nltk.download('stopwords')

def find_top_50_words(text):
    # Tokenize the text into words and convert to lowercase
    words = nltk.word_tokenize(text.lower())
    
    # Filter out punctuation
    words = [word for word in words if word.isalnum()]
    
    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Filter out the stopwords
    filtered_words = [word for word in words if word not in stop_words]
    
    # Count the frequency of each word
    word_counts = Counter(filtered_words)
    
    # Get the 50 most common words
    top_50_words = word_counts.most_common(50)
    
    return top_50_words

# Example usage
text = """
Robert Langdon is a famous character in various books and movies. 
He is known for his intelligence, problem-solving abilities, 
and knowledge of symbology. The character has appeared in several 
best-selling novels by author Dan Brown.
"""

top_words = find_top_50_words(text)
print(top_words)
