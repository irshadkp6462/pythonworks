age=int(input("enter the age:"))

weight=int(input("enter the weight:"))

height=int(input("enter the height:"))
           
gender=input("enter gender:").lower()

print(age,weight,height,gender)

if gender == "male":

    BMR= 10*weight + 6.25*height - 5*age + 5

elif gender == "female":

    BMR= 10*weight + 6.25*height -5*age -161

else:
      
      print("******enter valid gender****")

print(BMR)

activity_level=int(input("""
select avtivity level
enter 1 for sedentary
enter 2 for Lightly active
enter 3 for Moderately active
enter 4 for Very active
enter 5 for Extra avtive
"""))

if activity_level == 1:

   calories=BMR*1.2

elif  activity_level==2:

    calories=BMR*1.375

elif activity_level==3:

    calories=BMR*1.55

elif activity_level==4:

    calories=BMR*1.725

elif activity_level==5:

    calories=BMR*1.9


else:

    print("enter valid choice for activity level")

calories=round(calories,2)

print(f"total number of calories you need in order to maintain your current weight={calories}")

target_weight=int(input("enter the weight to reduce in kg"))

duration=int(input("enter duration in weeks"))

calorie_defi=target_weight*7700

day=duration*7

daily_calorie_defi=calorie_defi/day

print(daily_calorie_defi)

