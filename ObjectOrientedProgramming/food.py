
class Cusine:

    cusine_name:str

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

    def  display_cusine(self):

        print(self.cusine_name)

class MealType:

    meal_types:str

    def __init__(self,meal_types):

        self.meal_types=meal_types

    def mealtype_display(self):

        print(self.meal_types)

class Dish(MealType,Cusine):

    dish_name:str

    def __init__(self,dish_name):

        MealType.__init__(self,)

        self.dish_name=dish_name

    def dishtype_display(self):

        print(self.dish_name)
        







    