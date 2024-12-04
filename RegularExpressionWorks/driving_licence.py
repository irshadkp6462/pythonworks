from re import fullmatch

licence_num=input("enter the number")

pattern="(KL)[0-9]{2} [1-9][0-9]{3}[0-9]{7}"
matcher=fullmatch(pattern,licence_num)

if matcher==None:

    print("invalid")

else:

    print("valid")