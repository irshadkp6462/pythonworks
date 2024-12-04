class SuperHero:

    def __init__(self,name,species):

        self.name=name

        self.species=species

    def __str__(self):

        return self.name
    
class Spiderman(SuperHero):

    def __init__(self,name,species):

        super().__init__(name,species)

    def super_power(self):

        print("roar is the sound lion")

lion_instance=Spiderman("spiderman","spidersuit")

print(lion_instance)

lion_instance.super_power()
