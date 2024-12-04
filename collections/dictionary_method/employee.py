#create dictionary employee with keys eid,name,salary,department,experience

employee={"eid":101,"name":"siyad","salary":20000,"department":"manager","experience":2}

print(employee["salary"])

#add contact as 3456789

employee["contact"]=3456789


if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000


if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)