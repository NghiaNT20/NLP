'''17. How to extract all the pronouns in a text?
Q. Extract and print all the pronouns in the text

Input :

Desired Output :


 He
 He
 She
text="John is happy finally. He had landed his dream job finally. He told his mom. She was elated "
'''

# import re
# text="John is happy finally. He had landed his dream job finally. He told his mom. She was elated "
# pronouns = re.findall(r'\b(?:He|She)\b', text)
# print(pronouns)


# Using spacy's pos_ attribute to check for part of speech tags
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# def extract_pronouns(text):
#     # Process the text with spaCy
#     doc = nlp(text)
    
#     # Extract pronouns based on POS tag and print each on a new line
#     for token in doc:
#         if token.pos_ == "PRON":
#             print(token.text)
def extract_personal_pronouns(text):
    # Process the text with spaCy
    doc = nlp(text)
    
    # Extract only personal pronouns
    for token in doc:
        if token.pos_ == "PRON" and token.tag_ in {"PRP", "PRP$"}:
            if token.tag_ == "PRP":  # Personal pronouns only
                print(token.text)

# Example text
text = "John is happy finally. He had landed his dream job finally. He told his mom. She was elated."

# Extract and print the pronouns
extract_personal_pronouns(text)

# Output:
# He
# He
# She

