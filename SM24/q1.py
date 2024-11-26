""" 
    Question 1: Write a Python program that input a text file and outputs the
        number of words, characters, sentences in the file.( not use function)
Sample_text.txt:
    This is a sample text file.
    It contains several sentences.
    We can count words, characters, and sentences.
"""
# Open the file in read mode
file = open("Sample_text.txt", "r")
# Initialize the variables
words = 0
characters = 0
sentences = 0
# Loop through the file
for line in file:
    # Split the line into words
    words += len(line.split())
    # Count the characters
    characters += len(line)
    # Count the sentences
    sentences += line.count(".")
# Close the file
file.close()
# Print the results
print("Number of words:", words)
print("Number of characters:", characters)
print("Number of sentences:", sentences)


