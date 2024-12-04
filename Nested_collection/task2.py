student={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}

index=3

for i,element in enumerate(student):

    if i+1==index:

        mark=student.get(element)

        avg=sum(mark)/len(mark)

        print(avg)


student_avg={k:sum(v)/len(v) for k,v in student.items()}

print(student_avg)

