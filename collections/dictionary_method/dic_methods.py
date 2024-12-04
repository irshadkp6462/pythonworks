employee={"id":11,"name":"shibil","department":"hr","age":21,"salary":50000}

print(employee.get("age"))

print("shibil on air")

employee.pop("department")

print(employee)

for k in employee.keys():

    print(k)

for v in employee.values():

    print(v)

for k,v in employee.items():

    print(k,v)


    