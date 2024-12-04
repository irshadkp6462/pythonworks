f_year=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\year.txt","r")

f_centuary=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\leap_year.txt","w")

f_leap=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\centuary_year.txt","w")

for year in f_year:

    year=int(year)

    if year%100==0:

        f_centuary.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leap.write(str(year)+"\n")

f_year.close()

f_centuary.close()

f_leap.close()
     

