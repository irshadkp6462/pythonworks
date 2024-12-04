start=int(input("enter the number"))

end=int(input("enter the limit"))

if start<end:

    for num in range(start,end+1,1):

       print(num)

else:

    for num in range(start,end-1,1):
         print(num)