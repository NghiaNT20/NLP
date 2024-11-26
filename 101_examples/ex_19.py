'''Q. Find the similarity between any two text documents

Input :

    
text1="John lives in Canada"
text2="James lives in America, though he's not from there"
Desired Output :


 0.792817083631068
 '''
import spacy

nlp = spacy.load("en_core_web_lg")

doc1 = nlp("Jonh lives in Canada")
doc2 = nlp("James lives in America, through he's not from there")
doc1.similarity(doc2)

print(doc1.similarity(doc2))