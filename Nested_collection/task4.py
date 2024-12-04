user_input=input("enter the bracket pair ")

bracket_pairs={"{":"}","[":"]","(":")","<":">"}

symbol_stack=[]

top=-1

is_valid=True

for symbol in user_input:

    if symbol in bracket_pairs:

        top=top+1

        symbol_stack.append(symbol)

    elif symbol == bracket_pairs.get(symbol_stack[top]):
          
          top=top-1

          symbol_stack.pop()

    else:
         
         is_valid=False

if len(symbol_stack)==0 and is_valid==True:
     
     print("valid")

else:
     
     print("invalid")