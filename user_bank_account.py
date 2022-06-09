

class BankAccount:
    # don't forget to add some default values for these parameters!
    # Anything inside of a () when defining the functuins are called parameters 

    bank_name = "First National Dojo"
    all_accounts = []
    #anytime a bank account is created it creates an object
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        #Anytime an a object is made it is added to the list all_accounts
        BankAccount.all_accounts.append(self)




# Any function in a class is called a method

    def deposit(self, amount):
        self.balance += amount
        return self
        
        
    def withdraw(self, amount):
        self.balance -= amount
        return self
        
    def display_account_info(self):
        print(f"Balance is: {self.balance} Instris rate is: {self.int_rate}")
        return self

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    
    @classmethod
    def all_balances(cls):
        
        
        for account in cls.all_accounts:
            print(f"User account:{account.name} Balance is: {account.balance} Interest rate is:{account.int_rate}")
            
        


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=500)


    def display_info(self):
        print(f"{self.name} Balance is : {self.account.balance}")


#Anything inside of () when you are calling the function are called arguments
juan = User("Juan")
juan.account.deposit(20000).yield_interest().withdraw(1000)
juan.display_info()

cody = User("Cody")
cody.display_info()