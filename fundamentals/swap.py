#create a python file swap.py

#num1=100
#num2=200

#write a python prgrm to print swap these two numbers

num1=100
num2=200

#value b4 swapping num=100,num2=200

print(f"values b4 swapping num1={num1} num2={num2}")

#logic1 

#value after swapping num=100,num2=200

#temp=num1
#num1=num2
#num2=temp

#print(f"values after swapping num1={num1} num2={num2}")

#logic2 by adding and subs

num1=num1+num2 #num1=100+200=300
num2=num1-num2 #num2=300-100=100
num1=num1-num2 #num1=300-100=200

print(f"values after swapping logic2 num1={num1} num2={num2}")
