#create a dictionary product with keys id,title,price,brand

product={"id":12,"title":"boots","price":7999,"brand":"adidas"}

print(product["title"])

# update value of product

product["offer"]=6499

product["price"]=6999

print(product)

product["type"]="grass"

print(product)

#add offer as 10 if offer exit else add offer 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)