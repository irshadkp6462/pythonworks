arr1=[10,12,13,14,16]

arr2=[11,13,14,15]

arr1.sort()

arr2.sort()

p1=0

p2=0

while(p1<len(arr1)-1 or p2<len(arr2)-1):

    if arr1[p1]==arr2[p2]:

        print(arr1[p1])

        p1+=1

        p2+=1

    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr2[p2]<arr1[p1]:

        p2+=1

