
from re import findall

f=open("C:\\Users\\HP\\Desktop\\pythonworks\\RegularexpressionFileworks\\sample.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)