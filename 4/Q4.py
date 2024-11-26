'''Replace the pronouns in below text by the respective object nanes
Input:
text
My sister has a dog and she loves him"
Desired Output:
[My sister,she]
[a dog ,him]'''
import nltk
def identify_pronouns(text):
  pronouns = []
  nouns = []
  words = text.split()
  pos_tags = nltk.pos_tag(words)  # Requires installing NLTK library (nltk.org)

  for word, tag in pos_tags:
    if tag.startswith('PRP'):  # Check for pronouns (PRP, PRP$ etc.)
      pronouns.append(word)
    elif tag.startswith('NN'):  # Check for nouns (NN, NNS etc.)
      nouns.append(word)

  return pronouns, nouns

# Example usage
text = "My sister has a dog and she loves him"
pronouns, nouns = identify_pronouns(text)

print("Pronouns:", pronouns)
print("Nouns:", nouns)
words = text.split()
pos_tags = nltk.pos_tag(words)
print(pos_tags)
