lst=[1,2,3,4,5,6,7,8,9]

left=0

right=len(lst)-1

sum=8

while(left<right):

    cur_sum=lst[left]+lst[right]

    if cur_sum==sum:

        print(lst[left],lst[right])
        break
              
    elif  cur_sum>sum:

        right-1

    elif cur_sum<sum:

        left+1







