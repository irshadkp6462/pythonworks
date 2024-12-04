products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":6,"title":"iphone16promax","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles
print(len(products))


# print mobile titles

mobile_title=[p.get("title")for p in products]
print(mobile_title)

# print samsung mobiles
samsung_brand=[p.get("title") for p in products if p.get("brand")=="samsung"]

print(samsung_brand)


#costly product

print(max(products,key=lambda d:d.get("price")))

#cheap product

print(min(products,key=lambda d:d.get("price")))

#all costly mobile

costly_mobile=max(products,key=lambda d:d.get("price"))

max_costly=costly_mobile.get("price")

costly_mobiles=[m.get("title")for m in products if m.get("price")==max_costly]

print(costly_mobiles)

#count of samsung product 
samsung_brand=[p for p in products if p.get("brand")=="samsung"]

print(len(samsung_brand))

#brand name and count of brand

all_brands=[p.get( "brand" )for p in products]

brand_count={b:all_brands.count(b) for b in all_brands}

print(brand_count)

