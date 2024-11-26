'''Q. Find the similarity between any two text documents
Input :

    
text1="John lives in Canada"
text2="James lives in America, though he's not from there"
Desired Output :


 0.792817083631068
 '''

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similarity(text1, text2):
    # Combine the documents into a list
    documents = [text1, text2]
    
    # Create a TfidfVectorizer object
    tfidf_vectorizer = TfidfVectorizer()
    
    # Fit and transform the documents to a tf-idf matrix
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    
    # Compute the cosine similarity between the two documents
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    # The similarity is a 2D array, so we extract the value
    return similarity[0][0]

# Example usage
text1 = "John lives in Canada"
text2 = "James lives in America, though he's not from there"

similarity_score = find_similarity(text1, text2)
print(f"Similarity between the documents: {similarity_score}")

