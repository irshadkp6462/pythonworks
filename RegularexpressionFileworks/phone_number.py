f=open("C:\\Users\\HP\\Desktop\\pythonworks\\RegularexpressionFileworks\\phone_number.txt")

from re import fullmatch

for line in f:

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher != None:

        print(phone)

