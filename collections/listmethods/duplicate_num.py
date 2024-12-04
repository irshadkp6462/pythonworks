arr1=[1,2,2,2,1,4,5]

arr1.sort()

duplicate_num=[]

for i in range(0,len(arr1)-1):

    j=i+1

    result=arr1[j]-arr1[i]

    if result==0:

        if arr1[i] not in duplicate_num:

            duplicate_num.append(arr1[i])

print(duplicate_num)

