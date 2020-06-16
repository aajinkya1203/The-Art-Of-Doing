# all function definitions over here
def get_input():
    accounts['name'] = input("Hello, what is your name: ").title()
    accounts['savings'] = float(input("How much money would you like to set up your savings account with: "))
    accounts['checking'] = float(input("How much money would you like to set up your checking account with: "))

def show_details():
    print("\nCurrent Account Information:")
    for key, value in accounts.items():
        if key == 'name':
            print(key,":",value)
        else:
            print(key,": $",value)

def deposit( typeof ):
    cash = float(input("How much money would you like to deposit: "))
    accounts[typeof] += cash
    print("\nDeposited $",cash, "into", accounts['name'],"'s",typeof,'account!' )

def withdrawal( typeof ):
    cash = float(input("How much money would you like to withdraw: "))
    if accounts[typeof] - cash < 0:
        print("\nInsufficient Funds!")
    else:
        accounts[typeof] -= cash
        print("\nWithdrew $",cash, "from", accounts['name'],"'s",typeof,'account!' )

def continueAgain():
    choice = input("Would you like to make another transaction (y/n): ")
    if choice.startswith('y'):
        return True
    else:
        print("\nThanks for banking with us!")
        return False



print("Welcome to Aajinkya's National Bank!")


# setting up a dict to store user and his/her detials
accounts = {}

# setting a flag to exit outta the while loop
flag = True

# combining all functionalities

# getting the input of the user for his details only once
get_input()
while flag:
    # showing details at each run
    show_details()

    # accessing which type of account
    typeof = input("What account would you like to access (Savings or Checking): ").lower().strip()
    acc_type = ""
    if typeof.startswith('s'):
        acc_type = "savings"
    elif typeof.startswith('c'):
        acc_type = "checking"
    else:
        print("\nInvalid Input.\nTry again!")
        continue

    # what action would the user would like to perform
    action = input("What type of transaction would you like to make (Deposit or Withdrawal): ").lower()
    if action.startswith('d'):
        deposit( acc_type )
    elif action.startswith('w'):
        withdrawal( acc_type )
    else:
        print("Invalid input.\nTry again!")
        continue

    # asking user to continue or not
    flag = continueAgain()
    