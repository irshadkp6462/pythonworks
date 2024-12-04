f=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\fruits.txt","r")

fruits=[]

for  line in f:

    fruits.append(line.rstrip("\n"))
    
print(fruits)