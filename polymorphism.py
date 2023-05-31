
## Bank Application(Bank_v1 and Bank_v2) <<<Using method overloading (polymorphism)
#$ Here we want to update some details in my child class 

class Bank_v1:
    Bank_name='SBI'
    Bank_roi=7
    Bank_branch="Hyderabad"

    def __init__(self,name,age,account,balance):
        self.name=name
        self.age=age
        self.account=account
        self.balance=balance

    @classmethod
    def bank_details(cls):
        print(f"Bank Name Is {cls.Bank_name}")
        print(f"Bank ROI Is {cls.Bank_roi}")
        print(f"Bank Branch Is {cls.Bank_branch}")

    @staticmethod
    def get_int_value():
        value=int(input("Enter The Amount: "))
        return value

    @staticmethod
    def get_int():
        pin=int(input("Enter The Pin: "))
        return pin

    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print(f"Withdraw Successful And Remaining Balance Is {self.balance}")
        else:
            print("Insufficient Balance")

    def deposite(self):
        amount=self.get_int_value()
        self.balance+=amount
        print(f"Deposite Successful And Remaining Balance Is {self.balance}")

class Bank_v2(Bank_v1):
    Bank_branch="Bengaluru"
    Bank_IFSC="SBIN0010125"

    def __init__(self,name,age,account,balance,pin,adhar):
        self.name=name
        self.age=age
        self.account=account
        self.balance=balance
        self.pin=pin
        self.adhar=adhar

    def customer_details(self):
        print(f"Customer Name Is {self.name}")
        print(f"Customer Age Is {self.age}")
        print(f"Customer Account Number Is {self.account}")
        print(f"Customer Balance Is {self.balance}")
        print(f"Customer Adhar Number Is {self.adhar}")

    def withdraw(self):
        pin=self.get_int()
        if self.pin==pin:
            amount=self.get_int_value()
            if self.balance>=amount:
                self.balance-=amount
                print(f"Withdraw Successful And Remaining Balance Is {self.balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect Pin")


    @classmethod
    def bank_details(cls):
        print(f"Bank Name Is {cls.Bank_name}")
        print(f"Bank ROI Is {cls.Bank_roi}")
        print(f"Bank Branch Is {cls.Bank_branch}")
        print(f"Bank IFSC Number Is {cls.Bank_IFSC}")

    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.Bank_roi=newroi
        print(f"Updated ROI Is {cls.Bank_roi}")


obj1=Bank_v2("Tushar",25,36209,50000,9090,877764806367)
obj1.customer_details()
obj1.bank_details()
obj1.withdraw()

obj=Bank_v1("Biraaj",25,36209,50000)
obj.bank_details()







#$ ------------------------------------------------------------------------------------------







## Bank Application(Bank_v1 and Bank_v2) <<<Using method overloading (polymorphism) and chaining (super() or by class name)


class Bank_v1:
    bank_name='SBI'
    bank_roi=7
    bank_branch="Hyderabad"

    def __init__(self,n,a,ac,b):
        self.name=n
        self.age=a
        self.account=ac
        self.balance=b

    def customer_details(self):
        print(f"Customer Name Is {self.name}")
        print(f"Customer Age Is {self.age}")
        print(f"Customer Account Number Is {self.account}")
        print(f"Customer Balance Is {self.balance}")

    @classmethod
    def bank_details(cls):
        print(f"Bank Name Is {cls.bank_name}")
        print(f"Bank ROI Is {cls.bank_roi}")
        print(f"Bank Branch Is {cls.bank_branch}")

    @staticmethod
    def get_int_value():
        value=int(input("Enter The Amount: "))
        return value

    @staticmethod
    def get_int():
        pin=int(input("Enter The Pin: "))
        return pin

    def withdraw(self):
        amount=self.get_int_value()
        if self.balance>=amount:
            self.balance-=amount
            print(f"Withdraw Successful And Remaining Balance Is {self.balance}")
        else:
            print("Insufficient Balance")

    def deposite(self):
        amount=self.get_int_value()
        self.balance+=amount
        print(f"Deposite Successful And Remaining Balance Is {self.balance}")

class Bank_v2(Bank_v1):
    bank_branch="Bengaluru"
    bank_IFSC="SBIN0010125"

    def __init__(self,name,age,account,balance,pin,adhar): 
        super().__init__(name,age,account,balance)      
        self.pin=pin
        self.adhar=adhar

    def customer_details(self):
        super().customer_details()
        print(f"Customer Adhar Number Is {self.adhar}")

    def withdraw(self):
        pin=self.get_int()
        if self.pin==pin:
            super().withdraw()
        else:
            print("Incorrect Pin")


    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f"Bank IFSC Number Is {cls.bank_IFSC}")

    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print(f"Updated ROI Is {cls.Bank_roi}")


obj1=Bank_v2("Tushar",25,36209,50000,9090,877764806367)
obj1.customer_details()
obj1.bank_details()
obj1.withdraw()

