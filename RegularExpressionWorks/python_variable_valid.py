from re import fullmatch

user_input=input('enter the input')

# start with an alphabet(lower or upper case)
#any number of alphabet,digits,_

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")
    