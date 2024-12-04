text="this is a simple programming question to find word with maximum number of characters"

word=text.split()

def get_count(w):

    return word.count(w)

frequent_word=max(word,key=get_count)

print({frequent_word:word.count(frequent_word)})