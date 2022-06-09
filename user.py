# # declare a class and give it name User
# class User:	
#     bank_name = "First National Dojo"	
#     def __init__(self ):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# User()
# guido = User()
# monty = User()
# Accessing the instance's attributes

# print(guido.name)	# output: Michael
# print(monty.name)	# output: Michael


# guido.name = "Guido"
# print(guido.name) # output: Guido
# monty.name = "Monty"
# print(monty.name) # output: Monty


# guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name) # output: Dojo Credit Union 
# print(monty.bank_name) # output: First National Dojo

# User.bank_name = "Bank of Dojo"
# print(guido.bank_name) # output: Bank of Dojo 
# print(monty.bank_name) # output: Bank of Dojo




class User:		# here's what we have so far

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit

        print(f"User {self.name} deposited {amount}")
        print("============================================")
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        print(f"User {self.name} balance is {self.account_balance}")
        print("============================================")


    def make_withdrawal(self, amount):	
        print(f"User {self.name} withdrawal {amount}")

        print("============================================")

        self.account_balance -= amount	# the specific user's account decreases by the amount of the value received

        print(f"User {self.name} balance is {self.account_balance}")

        print("============================================")



guido = User("Guido", "Guidoitaly@gmail.com")
monty = User("Monty", "montyparis@aol.com")
# Accessing the instance's attributes
# print(guido.name)	
# print(monty.name)	


guido.make_deposit(1000)
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(50)

monty.make_deposit(500)
monty.make_deposit(100)
monty.make_withdrawal(50)
monty.make_withdrawal(100)







