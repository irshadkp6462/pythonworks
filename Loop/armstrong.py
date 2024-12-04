number=int(input("enter the number"))

digit_count=len(str(number))

original=number

total=0

while(number !=0):

    digit=number%10

    exponent=digit**digit_count

    total=total+exponent

    number=number//10

print("armstrong number" if total==original else "not armstrong number")
