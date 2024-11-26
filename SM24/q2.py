""" 
    Question 2: write a Python program that takes a sentences
        as input and outputs a new sentences where the FIRST and LAST words are SWAPPED.

"""
# Take the input from the user
sentence = input("Enter a sentence: ")
# Split the sentence into words
words = sentence.split()
# Swap the first and last words
words[0], words[-1] = words[-1], words[0]
# Join the words back together
new_sentence = " ".join(words)
# Print the new sentence
print("New sentence:", new_sentence)
