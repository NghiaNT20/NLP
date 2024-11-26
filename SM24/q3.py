""" 
    Question 3: Write a Python program that takes a document as 
        input and outputs a dictionary where the keys are the unique
        bigrams (two-word phrases) in the document and the values
        are the number of times each bigram appears.

"""
# Take the input from the user
document = input("Enter a document: ")
# Split the document into words
words = document.split()
# Initialize the dictionary
bigrams = {}
# Loop through the words
for i in range(len(words) - 1):
    # Get the bigram
    bigram = (words[i], words[i + 1])
    # Increment the count in the dictionary
    bigrams[bigram] = bigrams.get(bigram, 0) + 1
# Print the dictionary
print("Bigrams:", bigrams)
