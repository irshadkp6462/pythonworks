from re import finditer

text="ababababbabbaaababbaabba"

# pattern="a{2}"

# pattern="a{1,3}" 
pattern="*"# any number



matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())