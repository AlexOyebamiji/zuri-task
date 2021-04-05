import random

database = {} #dictionary

def init():
    
    print("Welcome to LEX_BANK")

    
    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
                
        login()
    elif(haveAccount == 2):
                
        print(register())
    else:
        print("You have selected invalid option")
        init()

def login():


    print("********* Login *********")

    

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                        
    print('Invalid account or password')
    login()

    

def register():
    print("****** Register *******")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself? \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("You account Has been created")
    print("== === ====== ==== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("== === ====== ==== ===")

    login()



def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
    
    SelectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(SelectedOption == 1):
        
        depositOperation()
    elif(SelectedOption == 2):
            
        withdrawalOperation()
    elif(SelectedOption == 3):
            
        logout()
    elif(SelectedOption == 4):
            
        exit()
    else:
        print("Invalid Option selected")
        bankOperation(user)

def withdrawalOperation():
    print("Your avaliable balance is 10000")
    withdrawalAmt = int(input("Enter the amount you want to withdraw: \n"))
    availableBalance = 10000
    if(withdrawalAmt > availableBalance):
        print("Insufficient Funds")
    elif withdrawalAmt == 0:
        print("Enter a valid Number")
    else:
        print("You can now collect your money \n Thanks for Banking with us")
    init()

def depositOperation():
    print("You have a previous balance of #10,000")
    depositedAmount = int(input("Enter the amount you want to deposit: \n"))
    previousBalance = 10000
    totalBalance = (previousBalance + depositedAmount)
    print("Your new account balance is: ", totalBalance)
    print("Thank you for banking with us")
    init()

def generationAccountNumber():
    
    return random.randrange(1111111111,8888888888)






def logout():
    login()

init()