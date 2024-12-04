f1=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\all_students.txt","r")

f2=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\failed.txt","r")

all_student=set()

failed=set()

for line in f1:

     line=line.rstrip("\n")

     all_student.add(line)

for line in f2:
     
     line=line.rstrip("\n")

     failed.add(line)

passed=all_student.difference(failed)

print(passed)

    

