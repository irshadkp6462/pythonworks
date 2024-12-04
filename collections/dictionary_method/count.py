text="ABBACB"

#print character count
#A:2
#B:3
#C:1

text_dictionary={}

for ch in text:

    if ch in text_dictionary:

        text_dictionary[ch]+=1

    else:

        text_dictionary[ch]=1

print(text_dictionary)

#task
#first recursive character B
#dictionary methods 