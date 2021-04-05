from datetime import datetime
import random

def core(isloggedIn,accountNo):
    '''
    This is the function for the core banking services
    :param isloggedIn:
    :param accountNo:
    :return:
    '''

    while(isloggedIn == True):
        print("\n*********ZuriBank Services*********")
        name = getCustname(db,accountNo)
        welcome_message(name)

        ##actions
        print("These are the available options:")
        print("0: Check Balance")
        print("1: Withdrawal")
        print("2: Cash Deposit")
        print("3: Complaint")
        print("4: Logout")

        selectedOption = int(input("Please select an option: > "))
        userBalance = getBalance(accountNo)

        if (selectedOption == 0):
            print("Your balance is ₦",userBalance)
        elif (selectedOption == 1):
            print("How much would you like to withdraw?")
            withdrawal=float(input("> ₦"))
            if (userBalance>withdrawal):
                newBalance = userBalance - withdrawal
                updateBalance(accountNo, newBalance)
                print("Available balance ₦", newBalance)
                print("take your cash")
            else:
                print("Account Balance insufficient!!")
        elif (selectedOption == 2):
            print("How much would you like to deposit?")
            deposit=float(input("> ₦"))
            newBalance= userBalance + deposit
            updateBalance(accountNo, newBalance)
            print("Available balance ₦", getBalance(accountNo))
        elif (selectedOption == 3):
            input("What issue will you like to report? \n> ")
            print("Your complaint has been assigned to appropriate team\nThank you for contacting us")
        elif (selectedOption == 4):
            isloggedIn=False
            print("You are now Logged out")
            break
        else:
            print("Invalid Option Selected, please try again")

def welcome_message(name):
    '''
    This method prints welcome message for customers
    :param name:
    '''
    print(today())
    print("Welcome %s" % name)

def today():
    '''
    This function gets the current date and time
    :return:
    '''
    now=datetime.now()
    return "Today: "+ now.strftime("%c")

def getBalance(accountNo):
    '''
    This function fetches the account balance from db
    :param accountNo:
    :return:
    '''
    return db[accountNo][3]

def updateBalance(accountNo, newBalance):
    '''
    This method updates account balance on the db
    :param accountNo:
    :param newBalance:
    :return:
    '''
    db[accountNo][3]=newBalance

def getCustname(db,accountNo):
    '''
    This function returns the first and last name of customer
    :param db:
    :param accountNo:
    :return:
    '''
    return db[accountNo][0]+" "+db[accountNo][1]

def generateAccNo():
    '''
    THis function generates a 10 digit account number
    :return:
    '''
    return random.randrange(1111111111,9999999999)

def login():
    '''
    This method allows a registered User to login and access services
    '''
    print("\n*********Login to ZuriBank*********")
    accountNo = int(input("Please enter your account Number\n> "))
    password = input("Please enter your password\n> ")
    if accountNo in db.keys() and db[accountNo][2] == password:
        # login successful
        isLoggedIn = True
        core(isLoggedIn, accountNo)
    else:
        print("Account NUmber or Password Incorrect.")

def register():
    '''
    This method allows a new User to register and access services
    '''
    print("\n*********Register New Accountk*********")
    print(">>>Please follow the steps below to create an account<<<")
    # open account bal =0 IsLoggedIn=True, ecore(isLoggedIn, accountNo)
    accountNo = generateAccNo()
    f_name = input("Please Enter your firstname> ")
    l_name = input("Please Enter your Lastname> ")
    pwd = input("Please Enter your preferred password> ")
    balance = 0.0
    print("Congratulation", f_name, l_name, "your account number", accountNo, "has been opened successfully")
    db[accountNo] = [f_name, l_name, pwd, balance]
    isloggedIn=True
    core(isloggedIn, accountNo)

## MAIN
while(True):
    #Global variable declaration
    #db = {usurAccountNo:[userFirstName, userLatName, userPaaaword, userBalance]}
    db={1234567890:["Seyi", "Zuri", "passwordSeyi", 50000.09]}

    print("============================")
    print("Welcome to ZuriBank mock ATM") # Welcome message
    print("----------------------------")

    #init_check
    check=int(input("Do you have an account with us? \nEnter 1 for yes Enter 2 for No\n> "))
    if check==1:
        login() # login & Access services

    elif check==2:
        register() # signup & Access services

    else:
        print("Invalid Option Selected, please try again")

    print("----------------------------")
    print("Thanks for banking with us!") # Outro message
    print("============================\n")