class GrandParent:

    def m(self):

        print("grandparent class m1 method")

class Parent:

    def m(self):

        print("parent class m2 method")

class Child(Parent,GrandParent):

    def m3(self):

        print("child class m3 method")

Child_instance=Child()

Child_instance.m3()

Child_instance.m()

Child_instance.m()