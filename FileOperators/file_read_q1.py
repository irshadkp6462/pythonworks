f=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\words.txt","r")

word=[]

for line in f:

    line=line.rstrip("\n")

    all_word=line.split(" ")

    for w in all_word:

        word.append(w)

        word_count={w:word.count(w) for w in word}

        sorted_word=[[v,k] for k,v in word_count.items()]

print(sorted(sorted_word,reverse=True))