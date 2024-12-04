word=["hello","hii","bye","heyy","bye","hii","hello","bye"]

word_frqzy={w:word.count(w) for w in word}

print(word_frqzy)

recursive_word=[k for k,v in word_frqzy.items() if v>1 ]

print(recursive_word)