f=open("C:\\Users\\HP\\Desktop\\pythonworks\\RegularexpressionFileworks\\hashtag.text")

from re import fullmatch,finditer

for line in f:
    
    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())
