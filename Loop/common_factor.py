
num1=int(input("enter the number"))

num2=int(input("enter the number"))

gcd=1

min_num=min(num1,num2)

for i in range(1,min_num+1):

    if num1%i==0 and num2%i==0:

        gcd=i

print(gcd)
