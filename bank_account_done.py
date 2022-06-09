class BankAccount:
    # don't forget to add some default values for these parameters!
    # Anything inside of a () when defining the functuins are called parameters 
    
    bank_name = "First National Dojo"
    all_accounts = []
    #anytime a bank account is created it creates an object
    def __init__(self, name, int_rate, balance): 
        self.name = name
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
        print(f"{self.name} Balance is: {self.balance} Instris rate is: {self.int_rate}")
        return self

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    
    @classmethod
    def all_balances(cls):
        
        
        for account in cls.all_accounts:
            print(f"User account:{account.name} Balance is: {account.balance} Interest rate is:{account.int_rate}")
            
        



        


#Anything inside of () when you are calling the function are called arguments
juan = BankAccount("Juan",.02,5000)
juan.deposit(1000).deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()



cody = BankAccount("Cody",.03,300000)

cody.deposit(1000).deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()




BankAccount.all_balances()