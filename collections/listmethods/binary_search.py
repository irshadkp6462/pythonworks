arr=[23,45,67,90,45,65]

arr.sort()

low=0

upp=len(arr)-1

is_present=False


search_element=int(input("enter the number: "))

while(low<=upp):

    mid=(low+upp)//2

    if search_element==arr[mid]:

        is_present=True
        break
 
    elif search_element<arr[mid]:

        upp=mid-1

    elif search_element>arr[mid]:

        low=mid+1

print(is_present)




