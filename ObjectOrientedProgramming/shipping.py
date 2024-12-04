class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*20)

class StandardShipping(ExpressShipping):

    def calculate_shipping_cost(self, weight):
        
        print(weight*10)

expe_instance=ExpressShipping()

expe_instance.calculate_shipping_cost(30)

std_instance=StandardShipping()

std_instance.calculate_shipping_cost(30)

ship_instance=Shipping()

ship_instance.calculate_shipping_cost(30)


