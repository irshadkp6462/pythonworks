text="ABSBDBDN"

#most recursive 

#non recursive

def get_count(char):
    
    return text.count(char)

most_fre=max(text,key=get_count)

print(most_fre)

least_recu=min(text,key=get_count)

print(least_recu)