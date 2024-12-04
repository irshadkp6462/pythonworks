class Employee:

    name:str

    rolnumber:int

    age:int

    course:str

    def set_student(self,name,rolnumber,age,course):

        self.name=name

        self.rolnumber=rolnumber

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.rolnumber,self.age)

stud_instance1=Employee()

stud_instance2=Employee()

stud_instance2.set_student("siyad",21,22)

stud_instance2.display()