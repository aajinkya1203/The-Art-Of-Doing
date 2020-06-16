# all function defination here
def get_input():
    temp = float(input("Enter a number: "))
    return temp

def addition( x, y ):
    sum = round(x + y, 2)
    print("The sum of", x, "and", y, "=", sum)
    calc = str(x) + ' + ' +str(y) + ' = ' + str(sum)
    history.append( calc )

def subraction( x, y ):
    sum = round(x - y, 2)
    print("The difference of", x, "and", y, "=", sum)
    calc = str(x) + ' - ' +str(y) + ' = ' + str(sum)
    history.append( calc )

def multiplication( x, y ):
    sum = round(x * y, 2)
    print("The product of", x, "and", y, "=", sum)
    calc = str(x) + ' * ' +str(y) + ' = ' + str(sum)
    history.append( calc )

def division( x, y ):
    if y == 0:
        history.append("DIV ERROR")
        print("Cannot divide by 0!")
        return None
    sum = round(x / y, 2)
    print("The quotient of", x, "and", y, "=", sum)
    calc = str(x) + ' / ' +str(y) + ' = ' + str(sum)
    history.append( calc )

def exponential( x, y ):
    sum = round(x ** y, 2)
    print("The result of", x, "raised to the power of", y, "=", sum)
    calc = str(x) + ' ^ ' +str(y) + ' = ' + str(sum)
    history.append( calc )

def continueAgain():
    choice = input("Would you like to continue again (y/n): ")
    if choice.startswith('y'):
        return True
    elif choice.startswith('n'):
        return show_history()
    else:
        history.append("INPUT ERROR!")
        return show_history()

def show_history():
    print("\nCalculation Summary:")
    for record in history:
        print(record)
    return False

print("Welcome to the The Python Calculator App!")

# creating a variable history to store all the records of the calculations
history = [ ]

# setting a flag to jump out of the while loop
flag = True

while flag:
    # getting input
    num_1 = get_input()
    num_2 = get_input()

    # asking which opp to perform
    operation = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower()
    if operation.startswith('a'):
        addition( num_1, num_2 )
    elif operation.startswith('s'):
        subraction( num_1, num_2 )
    elif operation.startswith('m'):
        multiplication( num_1, num_2 )
    elif operation.startswith('d'):
        division( num_1, num_2 )
    elif operation.startswith('e'):
        exponential( num_1, num_2 )
    else:
        print("\nInvalid input!")
        history.append( 'OPP ERROR!' )

    # asking user to continue or not
    flag = continueAgain()