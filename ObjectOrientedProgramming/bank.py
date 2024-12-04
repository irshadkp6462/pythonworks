class Bank:

    accno=int

    balance=int

    ac_type=str

    customer_name=str

    def __init__(self,accno,balance,ac_type,customer_name):

        self.accno=accno

        self.balance=balance

        self.ac_type=ac_type

        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account {self.accno} has been credited with amount {amount} avl balance {self.balance}")
    
    def withdraw(self,amount):

        if self.balance<amount:

            print("insufficient balance")

        else:

        
          self.balance-=amount

          print(f"your account {self.accno} has been debited with amount {amount} avl balance {self.balance}")

    def get_balance(self):

        print("your avl balance",self.balance)

customer_instance1=Bank(10000,2500,"savings","shibil")

customer_instance1.deposit(30)

customer_instance1.get_balance()
        