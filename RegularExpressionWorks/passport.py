from re import fullmatch

passport_num=input("enter the number")

pattern="[A-Z][1-9][0-9| ][0-9]{4}[1-9]"
matcher=fullmatch(pattern,passport_num)

if matcher==None:

    print("invalid")

else:

    print("valid")