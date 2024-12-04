f_read=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\p_words.txt","r")

f_palindrome=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\palindrome.txt","w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        f_palindrome.write(word+"\n")

f_palindrome.close()

f_read.close()


