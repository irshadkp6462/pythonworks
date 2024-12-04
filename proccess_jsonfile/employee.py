from json import load

f=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\employee.json")

data=load(f)

for emp in data:

   print(emp)
