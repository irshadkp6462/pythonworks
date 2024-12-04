from re import fullmatch

aadhar_num=input("enter the number")

pattern="[1-9]{1}[0-9]{3} [0-9]{4} [0-9]{4}"

matcher=fullmatch(pattern,aadhar_num)

if matcher==None:

    print("invalid")

else:

    print("valid")