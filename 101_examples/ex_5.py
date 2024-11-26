#How to tokenize a text using the 'tranformers' package?
'''Tokenize the given text in encoded form using the tokenizer of Huggingface’s transformer package.
text="I love spring season. I go hiking with my friends"'''
from transformers import AutoTokenizer

tokenizer= AutoTokenizer.from_pretrained('bert-base-uncased')

text="I love spring season. I go hiking with my friends"
inputs= tokenizer.encode(text)
print(inputs)
tokenizer.decode(inputs)