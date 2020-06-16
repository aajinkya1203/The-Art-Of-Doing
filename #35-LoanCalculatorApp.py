from matplotlib import pyplot
# all function definitions here
def get_input():
    user['principal'] = float(input("Enter the loan amount: "))
    user['rate'] = float(input("Enter the interest rate: ")) / 100.0
    user['monthly'] = float(input("Enter the desired monthly payment amount: "))
    return user['principal']

def show_info(months):
    print('\n\n----Loan information after {} months----'.format(months))
    for key, value in user.items():
        print(key,":",value)

def add_interest():
    user['principal'] += ( user['principal'] * user['rate'] ) / 12

def make_payment():
    add_interest()
    # checking if principal > 0 or not after subracting monthly pay
    if user['principal'] - user['monthly'] > 0:
        user['principal'] -= user['monthly']
        user['paid'] += user['monthly']
        return True
    elif user['principal'] - user['monthly'] < 0:
        user['paid'] += user['principal']
        user['principal'] = 0
        return False
    else:
        user['principal'] -= user['monthly']
        user['paid'] += user['monthly']
        return False

def check_possibility(months):
    show_info(months)
    input("Press any key to start paying off your loan!")
    # copy the initial principal+interest into a var to see if the person can pay of loan
    temp = user['principal'] + ( user['principal'] * user['rate'] ) / 12
    if temp - user['monthly']  > initial_principal:
        user['principal'] = temp
        show_info(months)
        print("\nYou will never pay off your loan!!!\nYou cannot get ahead of the interest! :-(")
        return False
    else:
        return True

def summarize(months, initial):
    print(f"\n\nCongratulations! You paid off your loan in {months} months!")
    print(f"Your initial loan was ${initial} at a rate of { user['rate'] * 100 }%.")
    print(f"Your monthly payment was ${ user['monthly'] }")
    print(f"You spent ${ round( user['paid'], 2 ) } total.")
    print(f"You spent ${ round( user['paid'] - initial, 2 ) } on interest!")

def create_graph(data_set):
    # creating vars for x and y axis
    x_values = []
    y_values = []
    for data in data_set:
        x_values.append( data[0] )
        y_values.append( data[1] )
    pyplot.plot( x_values, y_values )
    pyplot.title( f"{ user['rate']}% Interest with ${ user['monthly'] } Monthly Paymen" )
    pyplot.xlabel( "Month Number" )
    pyplot.ylabel( "Principal Of Loan" )
    pyplot.show()

print("Welcome to the Loan Calculator App!")

# creating a dict to store user info
user = {
    'principal': 0,
    'rate': 0,
    'monthly': 0,
    'paid': 0,
}

# storing the initial principal
initial_principal = 0

# flag to exit while loop
paying = True

# var to keep track of months paid
months = 0

# creating a list of tuples to be used for creating the graph
data_list = []

# compiling all the code here

# getting user input
initial_principal = get_input()

# checking possibility
paying = check_possibility(months)

# if possible, paying = True else False and accordingly the code will/will not jump into the while loop

while paying:
    # making payment
    paying = make_payment()

    # increasing the counter months
    months += 1

    # appending data to the list which will be used to create the graph
    data = ( months, user['principal'] )
    data_list.append(data)

    # showing details
    show_info(months)

    if paying == False:
        summarize(months, initial_principal)
        create_graph( data_list )
