def sort_number(*args,**kwargs):

    if kwargs.get("reversed")=="True":

        return sorted(args,reverse=True)
    
    if kwargs.get("reversed")=="False":

        return sorted(args)
    
print(sort_number(1,2,6,4,15,11,reversed="True"))

print(sort_number(1,2,6,4,15,11,reversed="False"))