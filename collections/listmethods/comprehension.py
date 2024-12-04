
# [return iteration condition] 

arr=[2,3,4,5,6,7]

square=[num**2 for num in arr]

print(square)

even_number=[num for num in arr if num%2==0]

print(even_number)

odd_num=[num for num in arr if num%2!=0]

print(odd_num)

num_gt_five=[num for num in arr if num>5]

print(num_gt_five)

text=["apple","orange","grape","watermelone"]


#longest word 

long=max([len(w) for w in text ])

longest_word=[w for w in text if len(w)==long]

print(longest_word)