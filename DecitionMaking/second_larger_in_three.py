
num1=int(input("enter first num:"))

num2=int(input("enter second num:"))

num3=int(input("enter third num:"))

if  num1>num2 and num1>num3: 
        
    if num2>num3:

        print("num2 is second largest")

    else:
         
        print("num3 is second largest")

if  num2>num1 and num2>num3: 
        
    if num1>num3:

        print("num1 is second largest")

    else:
         
        print("num3 is second largest")


if  num3>num1 and num3>num2: 
        
    if num1>num2:

        print("num1 is second largest")

    else:
         
        print("num2 is second largest")


