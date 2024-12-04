arr=[10,20,10,30,40,50,40]

st=set()

for num in arr:

    st.add(num)

print(st)

st1={10,20,30,40,50}

st2={60,70,10,80,20}

intersection_set=st1.intersection(st2)

print(intersection_set)

union_set=st1.union(st2)

print(union_set)

dif=st1.difference(st2)

print(dif)

st10={1,2,3}

st11={1,2,3,4,5}

print(st10.issubset(st11))


sym_dif=st1.symmetric_difference(st2)

print(sym_dif)

st1.update(st2)

print(st1)

