from re import finditer

text="I have 3 cars,2 bike- and 1 cycle"

# pattern="\w" #[a-zA-Z0-9] or \w for alphanumeric

# pattern="\d" #[0-9] or \d for numeric

# pattern="\D" # exclude digits

# pattern="\W" #special characters

# pattern="\s" #white space

pattern="\S" # exclude white space

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())