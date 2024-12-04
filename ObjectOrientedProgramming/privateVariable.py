class BankAccount:

    def __init__(self,customer_name,mpin,bank_type,balance):

        self.customer_name=customer_name

        self.__mpin=mpin

        self.bank_type=bank_type

        self.__balance=balance

    def get_balance(self):

            print(self.__balance)

    def __str__(self):
         
         return self.customer_name
    
bank_acc_instance=BankAccount("hari",1234,"savings",50000)

bank_acc_instance.get_balance()