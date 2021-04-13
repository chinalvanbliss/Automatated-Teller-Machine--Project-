<<<<<<< Updated upstream
# Automated Teller Machine (ATM) Simulation Project II


# For  import of random account number generator for potential Ubuntu customers.
import random

# For import of transaction date and time especially login information.
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Database for account REGISTRATION such as firstname, middle name, lastname, NiMC number, phone, email and password.
database = {}

# Database for existing Ubuntu Account holders.
database_ubuntu = {'Adefunmi': 'password5555', 'Alvan' : 'password8989', 'Chinwendu': 'password5865'}


# Ubuntu Bank ATM Initialization Function.
def init():
    print('======================')
    print('Welcome to Ubuntu Bank')
    print('======================')

    ubuntu_account = int(input('Do you have an Ubuntu Account? \n 1. (Yes) \n 2. (No) \n'))

    if ubuntu_account == 1:
        ubuntu_login()

    elif ubuntu_account == 2:
        register()

    else:
        print('You have selected an invalid option')
        init()


# Login and authentication for old Ubuntu Account holders in database viz: Adefunmi, Alvan and Chinwendu.
def ubuntu_login():
    name = input("Please enter your name: \n")
    password = input('Enter your password: \n')
    if name in database_ubuntu and password == database_ubuntu[name]:
        print("Login Date and Time =", dt_string)
        print('===========================================')
        print("Welcome to Ubuntu ATM Service " + name)
        print('===========================================')
        ubuntu_existing_accounts()
        return True

    else:
        print("Password or Username Incorrect. Please try again")
        ubuntu_login()
        return False


# Bank operations/services for old account holders at Ubuntu bank.
def ubuntu_existing_accounts():
    ubuntu_serv = int(input("Please select a service: \n 1. Deposit \n 2. Withdrawal \n 3. Complaint \n 4. Logout \n"))

    if ubuntu_serv == 1:
        deposit()
    elif ubuntu_serv == 2:
        withdrawal()
    elif ubuntu_serv == 3:
        complaint()
    elif ubuntu_serv == 4:
        logout()
    else:
        print('Invalid service option selected')
        ubuntu_existing_accounts()


# Bank Login/Authentication Function for REGISTER Account Customers.
def login():
    print('******** Login ********')
    user_account_number = int(input('Enter your Ubuntu account number: \n'))
    password = int(input('Enter your Ubuntu account password: \n'))
    for account_number, user_details in database.items():
        if account_number == user_account_number:
            if user_details[6] == password:
                ubuntu_service(user_details)
            else:
                print('\nInvalid password')
                init()
    else:
        print('Invalid Ubuntu Account Number, please enter correctly or register to continue')
        init()


# Ubuntu Bank Customer Operations for REGISTER customers comprising: Deposit, Withdrawal, Complaint, Logout and Exit).
def ubuntu_service(user):
    print("Login Date and Time =", dt_string)
    print("===================================================")
    print('Welcome to Ubuntu ATM service %s' % (user[0]))
    print("=================================================\n")
    service_option = int(input("Please select service: \n 1. Deposit \n 2. Withdrawal \n 3. Complaint \n 4. Logout \n"))

    if service_option == 1:
        deposit()
    elif service_option == 2:
        withdrawal()
    elif service_option == 3:
        complaint()
    elif service_option == 4:
        print('Thanks for banking with Ubuntu, have a nice day')
        logout()
    else:
        print('Invalid service option selected')
        ubuntu_service(user)


# Ubuntu Account Registration and Generation Functions.
def register():
    print('******** Register for Ubuntu Account ********')
    first_name = input('Enter your first name \n')
    middle_name = input('Enter your middle name \n')
    last_name = input('Enter your last name \n')
    nationalID_number = int(input('Enter your NiMC NIN \n'))
    mobile_number = int(input('Enter your mobile number \n'))
    email = input('Enter email address \n')
    password = int(input('Create a password for your Ubuntu account \n'))

    def account_number_generation():
        return random.randrange(0000000000, 9999999999)

    ubuntu_account_number = account_number_generation()
    database[ubuntu_account_number] = [first_name, middle_name, last_name, nationalID_number, mobile_number, email, password]
    print('Your Ubuntu savings account number has been created')
    print('===================================================================')
    print('Your Ubuntu savings account number is: %d' % ubuntu_account_number)
    print('Please keep your account details private and safe')
    print('===================================================================')
    login()


# Ubuntu deposit service function.
def deposit():
    print('******** Deposit Service ********')
    account_balance = 0.00
    print('Your account_balance is NGN', account_balance)
    deposit_amount = float(input('How much would you like to deposit? \n'))
    total_fund = account_balance + deposit_amount
    print("Your account balance is", total_fund)
    print('Transaction successful, thanks for banking with Ubuntu')
    additional_transaction()


# Ubuntu withdrawal service function.
def withdrawal():
    print('******** Withdrawal ********')
    account_balance = 98746
    print("Your account_balance is", account_balance)
    amount = float(input("Enter amount to withdraw \n"))
    if amount < account_balance:
        print("Transaction successful, please take your cash")
    elif amount > account_balance:
        print('Insufficient fund, please try again')
    additional_transaction()


# Ubuntu complaint service function.
def complaint():
    print('******** Complaint Service ********')
    print('========================================================')
    input("We are here to help, what issue would you like to report? \n")
    print('========================================================')
    print('Complaint received, we will find a solution as soon as possible. Thank you for contacting us.')
    additional_transaction()


# Function to continue and discontinue bank transaction, services or operations for all customer categories.
def additional_transaction():
    print('Do you wish to perform another transaction?')
    add_option = int(input("Please select option: \n 1. New-Transaction \n 2. Exit-Transaction \n"))
    if add_option == 1:
        option = int(input("Please select transaction: \n 1. Deposit \n 2. Withdrawal \n 3. Complaint \n 4. Logout \n"))
        if option == 1:
            deposit()
        elif option == 2:
            withdrawal()
        elif option == 3:
            complaint()
        elif option == 4:
            logout()
        else:
            print('Invalid option, please select a valid option')
            additional_transaction()
    elif add_option == 2:
        logout()
    else:
        print('Invalid option, please select a valid option')
        additional_transaction()


# Exits bank operations, transactions or services for both newly REGISTERED and OLD customers.
def logout():
    print('Thanks for banking with Ubuntu, have a nice day')
    exit()


# Initializes ATM operation.
init()
=======
# Automated Teller Machine (ATM) Simulation Project II


# For  import of random account number generator for potential Ubuntu customers.
import random

# For import of transaction date and time especially login information.
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Database for account REGISTRATION such as firstname, middle name, lastname, NiMC number, phone, email and password.
database = {}

# Database for existing Ubuntu Account holders.
database_ubuntu = {'Adefunmi': 'password5555', 'Alvan' : 'password8989', 'Chinwendu': 'password5865'}


# Ubuntu Bank ATM Initialization Function.
def init():
    print('======================')
    print('Welcome to Ubuntu Bank')
    print('======================')

    ubuntu_account = int(input('Do you have an Ubuntu Account? \n 1. (Yes) \n 2. (No) \n'))

    if ubuntu_account == 1:
        ubuntu_login()

    elif ubuntu_account == 2:
        register()

    else:
        print('You have selected an invalid option')
        init()


# Login and authentication for old Ubuntu Account holders in database viz: Adefunmi, Alvan and Chinwendu.
def ubuntu_login():
    name = input("Please enter your name: \n")
    password = input('Enter your password: \n')
    if name in database_ubuntu and password == database_ubuntu[name]:
        print("Login Date and Time =", dt_string)
        print('===========================================')
        print("Welcome to Ubuntu ATM Service " + name)
        print('===========================================')
        ubuntu_existing_accounts()
        return True

    else:
        print("Password or Username Incorrect. Please try again")
        ubuntu_login()
        return False


# Bank operations/services for old account holders at Ubuntu bank.
def ubuntu_existing_accounts():
    ubuntu_serv = int(input("Please select a service: \n 1. Deposit \n 2. Withdrawal \n 3. Complaint \n 4. Logout \n"))

    if ubuntu_serv == 1:
        deposit()
    elif ubuntu_serv == 2:
        withdrawal()
    elif ubuntu_serv == 3:
        complaint()
    elif ubuntu_serv == 4:
        logout()
    else:
        print('Invalid service option selected')
        ubuntu_existing_accounts()


# Bank Login/Authentication Function for REGISTER Account Customers.
def login():
    print('******** Login ********')
    user_account_number = int(input('Enter your Ubuntu account number: \n'))
    password = int(input('Enter your Ubuntu account password: \n'))
    for account_number, user_details in database.items():
        if account_number == user_account_number:
            if user_details[6] == password:
                ubuntu_service(user_details)
            else:
                print('\nInvalid password')
                init()
    else:
        print('Invalid Ubuntu Account Number, please enter correctly or register to continue')
        init()


# Ubuntu Bank Customer Operations for REGISTER customers comprising: Deposit, Withdrawal, Complaint, Logout and Exit).
def ubuntu_service(user):
    print("Login Date and Time =", dt_string)
    print("===================================================")
    print('Welcome to Ubuntu ATM service %s' % (user[0]))
    print("=================================================\n")
    service_option = int(input("Please select service: \n 1. Deposit \n 2. Withdrawal \n 3. Complaint \n 4. Logout \n"))

    if service_option == 1:
        deposit()
    elif service_option == 2:
        withdrawal()
    elif service_option == 3:
        complaint()
    elif service_option == 4:
        print('Thanks for banking with Ubuntu, have a nice day')
        logout()
    else:
        print('Invalid service option selected')
        ubuntu_service(user)


# Ubuntu Account Registration and Generation Functions.
def register():
    print('******** Register for Ubuntu Account ********')
    first_name = input('Enter your first name \n')
    middle_name = input('Enter your middle name \n')
    last_name = input('Enter your last name \n')
    nationalID_number = int(input('Enter your NiMC NIN \n'))
    mobile_number = int(input('Enter your mobile number \n'))
    email = input('Enter email address \n')
    password = int(input('Create a password for your Ubuntu account \n'))

    def account_number_generation():
        return random.randrange(0000000000, 9999999999)

    ubuntu_account_number = account_number_generation()
    database[ubuntu_account_number] = [first_name, middle_name, last_name, nationalID_number, mobile_number, email, password]
    print('Your Ubuntu savings account number has been created')
    print('===================================================================')
    print('Your Ubuntu savings account number is: %d' % ubuntu_account_number)
    print('Please keep your account details private and safe')
    print('===================================================================')
    login()


# Ubuntu deposit service function.
def deposit():
    print('******** Deposit Service ********')
    account_balance = 0.00
    print('Your account_balance is NGN', account_balance)
    deposit_amount = float(input('How much would you like to deposit? \n'))
    total_fund = account_balance + deposit_amount
    print("Your account balance is", total_fund)
    print('Transaction successful, thanks for banking with Ubuntu')
    additional_transaction()


# Ubuntu withdrawal service function.
def withdrawal():
    print('******** Withdrawal ********')
    account_balance = 98746
    print("Your account_balance is", account_balance)
    amount = float(input("Enter amount to withdraw \n"))
    if amount < account_balance:
        print("Transaction successful, please take your cash")
    elif amount > account_balance:
        print('Insufficient fund, please try again')
    additional_transaction()


# Ubuntu complaint service function.
def complaint():
    print('******** Complaint Service ********')
    print('========================================================')
    input("We are here to help, what issue would you like to report? \n")
    print('========================================================')
    print('Complaint received, we will find a solution as soon as possible. Thank you for contacting us.')
    additional_transaction()


# Function to continue and discontinue bank transaction, services or operations for all customer categories.
def additional_transaction():
    print('Do you wish to perform another transaction?')
    add_option = int(input("Please select option: \n 1. New-Transaction \n 2. Exit-Transaction \n"))
    if add_option == 1:
        option = int(input("Please select transaction: \n 1. Deposit \n 2. Withdrawal \n 3. Complaint \n 4. Logout \n"))
        if option == 1:
            deposit()
        elif option == 2:
            withdrawal()
        elif option == 3:
            complaint()
        elif option == 4:
            logout()
        else:
            print('Invalid option, please select a valid option')
            additional_transaction()
    elif add_option == 2:
        logout()
    else:
        print('Invalid option, please select a valid option')
        additional_transaction()


# Exits bank operations, transactions or services for both newly REGISTERED and OLD customers.
def logout():
    print('Thanks for banking with Ubuntu, have a nice day')
    exit()


# Initializes ATM operation.
init()
>>>>>>> Stashed changes
