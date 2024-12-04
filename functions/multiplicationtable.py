def multiplication_table(number,n=10):

    for i in range(1,n+1):

        print(f"{i} * {number} = {i*number}")

multiplication_table(3)

#create a function exponent with two parameter num1,1

def expo(number,n=2):
     
    return number**n

print(expo(6))


#print numbers from start to end
# random_numbers(1,7,2)#1,3,5

def random_numbers(start,end,step=1):

    while(start <=end):

        print(start)

        start=start+step

random_numbers(10,100,2) 