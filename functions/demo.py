#create a function last_digit_max with two param num1
#num1=123
#num2=872
#num1

def last_didgit_max(num1,num2):

    num1_last_digit=num1%10

    num2_last_digit=num2%10

    print(num1 if num1_last_digit>num2_last_digit else num2)

print(last_didgit_max(123,871))