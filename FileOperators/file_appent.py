f=open("C:\\Users\\HP\\Desktop\\pythonworks\\DataSets\\frame_work.txt","a")

frame_work=["wordpress","springboot","fastapi","oodo"]

for fw in frame_work:

    f.write("\n"+fw)

f.close()