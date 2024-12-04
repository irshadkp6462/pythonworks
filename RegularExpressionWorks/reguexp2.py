from re import finditer

text="i have 3 cars,2 bike- and 1 cycle"

pattern="[^akA-Z0-9, /-]"

# pattern="[a-z]" #lowercase alphabets
# pattern="[A-Z]" #uppercasecase alphabets
# pattern="[a-zA-Z]" #alphabets
# pattern="[0-9]"
# pattern="[a-zA-Z0-9]" alphanumeric
#pattern="[^a-zA-Z0-9]" special characters
# predefined characters
# quantifiers

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())