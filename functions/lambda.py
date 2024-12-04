#lambda function to add 2 numbers

add=lambda n1,n2:n1+n2

print(add(110,3))

#lambda function to sub 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(110,3))

#lambda function to find cube of a number

cube=lambda n:n**3

print(cube(3))

max_two=lambda str1,str2: str1 if len(str1) > len(str2) else str2 

print(max_two("haaaai","byee"))

min_two=lambda str1,str2: str2 if len(str1) > len(str2) else str1

print(min_two("haaaai","byee"))


smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1

print(smart_sub(29,22))



words=["haai","helooo","bye","morning","test","apple"]


get_lenght=lambda word:len(word)
print(max(words,key=get_lenght))


text="this is a simple programming question to find word with maximum number of characters"

word=text.split()

def get_length(w):
    
    return len(w)

srt_words=sorted(word,key=get_length,reverse=True)

print(srt_words)

