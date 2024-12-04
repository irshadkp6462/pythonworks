f=open("C:\\Users\\HP\\Desktop\\pythonworks\\RegularexpressionFileworks\\text.txt")

from re import findall

date=f.read()

#pattern="\d+/\d+/\d+"

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,date)

for d in dates:

    print(d)
