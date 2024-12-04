num1=int(input("enter the num"))

num2=int(input("enter the num"))

try: 
    result=num1/num2

    print(result)

except Exception as e:

    print(e)

    num2=int(input("enter another number"))

    result=num1/num2

    print(result)

finally:

    print("file operation")

    print("database commit")