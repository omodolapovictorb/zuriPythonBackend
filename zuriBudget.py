


class Budget:
    '''
    Budget Class for deposit, withdrawal, showing balance and transferring balance
    '''
    availableBalance = 0.0 # initial balance is 0
    budgetName = ""

    def __init__(self, name, initialBalance):
        self.budgetName = name
        self.availableBalance += initialBalance

    def deposit(self,amount):
        self.availableBalance += amount
        print("#", amount, "Deposit into", self.budgetName, " Successful!")
        print(self.budgetName, "available balance is #", self.availableBalance)

    def withdraw(self,amount):
        if amount>self.availableBalance:
            print(self.budgetName, "Balance Insufficient")
        else:
            self.availableBalance -= amount
            print("#", amount, "Withdrawal from", self.budgetName, "Successful!")

    def show_balance(self):
        print(self.budgetName, "available balance is #", self.availableBalance)

    def transfer(self, recepient, amount):
        if amount>self.availableBalance:
            print(self.budgetName, "Balance Insufficient")
        else:
            self.availableBalance -= amount
            recepient.availableBalance += amount
            print("#", amount, "Transfer from", self.budgetName, "to", recepient.budgetName, " Successful!")

#########main

#object initialization
print(">>>>>>>zuriBudgetClass<<<<<<<")
print(">>>>>>>Initializing objects of Budget Class")
food = Budget("food", 500)
clothing = Budget("clothing",48)
entertainment = Budget("entertainment", 200)

#initial Balance
print("\n>>>>>>>Showing available balance for each category")
food.show_balance()
clothing.show_balance()
entertainment.show_balance()

#Deposit 200 into food
print("\n>>>>>>>Deposit #50 into clothing")
clothing.deposit(50)

#withdraw 20 from each catergory
print("\n>>>>>>>Withdrawing #20 from each category")
food.withdraw(20)
clothing.withdraw(20)
entertainment.withdraw(15)


#compute category of each category
print("\n>>>>>>>Showing available balance for each category")
food.show_balance()
clothing.show_balance()
entertainment.show_balance()

# transfer balance amount between categories
print("\n>>>>>>>Transfer #89.5 from entertainment to food")
entertainment.transfer(food,89.5)

#compute category of each category
print("\n>>>>>>>Showing available balance for each category")
food.show_balance()
clothing.show_balance()
entertainment.show_balance()