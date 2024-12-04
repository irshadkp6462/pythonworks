class Movie:

    id=int

    title:str

    rating:int

    run_time:int

    director:str

    genre=str

    def __init__(self,id,title,rating,run_time,director,genre):
        
        self.id=id

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def display(self):

        print(self.id,self.title,self.rating,self.director)

film_instance1=Movie()

film_instance2=Movie(100,"arm",4.5,"jithin lal",120,"action")

film_instance2.display