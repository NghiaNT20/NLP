'''Write code to print out an index for a lexicon, allowing someone to look up words according
to their meanings (or their pronunciations; whatever properties are contained in the lexical entries).'''


def get_meaning(word):
    for meaning, words in lexicon.items():
        if word in words:
            return meaning
    return None
lexicon = {
    "good": ["acceptable", "excellent", "great","positive","good"],
    "bad": ["awful", "poor", "terrible","bad"],
    "healthy": ["fresh", "strong", "lively","healthy"],
    # Add more meanings and words as needed
}


word = "awful"
result = get_meaning(word)
print(result)
