class Budget:
    
    def __init__(self, category, amount):

        self.category = category
        self.amount = amount

    def deposit(self):

        amount = self.amount
        x = int(input("How much would you like to deposit?\n"))

        account_balance = amount + x
        print("Thank you, your new account balance is %d" %account_balance)

    def withdraw(self):
        amount = self.amount
        y = int(input("How much do you want to withdraw? \n"))

        account_balance = amount - y
        print("Please wait ...")
        print("Your new balance is %d" %account_balance)
        print("Thank you for using bank")


    def transfer(self):
        amount = self.amount
        e = int(input("How much would you like to transfer? \n"))

        if (amount >= e):
            print("Please wait while we complete transaction")

            account_balance = amount - e
            print("Your account balance is %d" %account_balance)




    def check_balance(self):
        amount = self.amount
        amount = account_balance

        print("Your budget balance is %d" %account_balance)

category = Budget("Clothing", 4000)
category_1 = Budget("Food", 3200)
category_2 = Budget("Entertainment", 5000)


category_1.transfer()
