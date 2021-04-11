from datetime import datetime

def logic(userId, balances):
    ##actions
    print("These are the available options:")
    print("0: Check Balance")
    print("1: Withdrawal")
    print("2: Cash Deposit")
    print("3: Complaint")

    selectedOption = int(input("Please select an option: > "))
    userBalance = balances[userId]

    if (selectedOption == 0):
        print("Your balance is ₦",userBalance)
    elif (selectedOption == 1):
        print("How much would you like to withdraw?")
        withdrawal=float(input("> ₦"))
        newBalance= userBalance-withdrawal
        updateBalance(userId, balances, newBalance)
        if (userBalance>withdrawal):
            print("take your cash")
        else:
            print("Account Balance insufficient!!")
    elif (selectedOption == 2):
        print("How much would you like to deposit?")
        deposit=float(input("> ₦"))
        newBalance= userBalance + deposit
        updateBalance(userId, balances, newBalance)
        print("Current balance ₦", balances[userId])
    elif (selectedOption == 3):
        input("What issue will you like to report? \n> ")
        print("Thank you for contacting us")
    else:
        print("Invalid Option Selected, please try again")

def core(allowedUsers,allowedPassword, balances):
    name = input("What is your Name? \n> ")
    if (name in allowedUsers):
        userId = allowedUsers.index(name)
        password = input("Your password? \n> ")

        if (password == allowedPassword[userId]):

            printDatetime()
            print("Welcome %s" % name)

            #logic function goes here
            logic(userId, balances)

        else:
            print("Password incorrect, please try again")
    else:
        print("Username incorrect, please try again")

def printDatetime():
    now=datetime.now()
    print("Today: ",now.strftime("%c"))

def updateBalance(userId, balances, newBalance):
    balances[userId]=newBalance





## MAIN
while(True):
    #Global variable declaration
    allowedUsers = ['Seyi', 'Mike', 'Love']
    allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']
    balances=[200,300,600]

    print("========================")
    print("Welcome to Zuri mock ATM") # Welcome message
    print("------------------------")

    core(allowedUsers,allowedPassword, balances)

    print("------------------------")
    print("Thanks for banking with us") # Welcome message
    print("========================\n")