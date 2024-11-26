""" 
    Question 4: Write a Python program that takes a paragraph
        of text as input and outputs the number of times each word
        appears in the paragraph.

"""
# Take the input from the user
paragraph = input("Enter a paragraph: ")
# Split the paragraph into words
words = paragraph.split()
# Initialize the dictionary
word_counts = {}
# Loop through the words
for word in words:
    # Increment the count in the dictionary
    word_counts[word] = word_counts.get(word, 0) + 1
# Print the dictionary

print("Word counts:", word_counts)