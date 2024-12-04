from json import load

f=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\countries.json",encoding="utf-8")

data=load(f)

#print(len(data))

all_country_name=[country.get("name") for country in data]

#print(all_country_name)

all_region=[country.get("region") for country in data]

#print(set(all_region))

region_count={region:all_region.count(region) for region in all_region}

#print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))

#print(max_region_count,region_count.get(max_region_count))

#country_name=input("enter the country")

country_capital=[country.get("capital")for country in data if country.get("name")=="India"]

#print(country_capital)

country_borders={country.get("name"):len(country.get("borders",[])) for country in data}

#print(country_borders)

max_border=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

#print(max_border)

max_population=max(data,key=lambda country:country.get("population",[])).get("name")

#print(max_population)

alpha_3_code=[country.get("borders") for country in data if country.get("name")=="India"][0]

#print(indian_border)

for code in  alpha_3_code:

    for country in data:

        if country.get("alpha3Code")==code:

          print(country.get("name"))