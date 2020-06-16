print("Welcome to the Factor Generator App!")

# using a list to store all the factors to show the summary
factors = []

# setting a flag to jump out of the while loop
rewind = True

while rewind:
    user_input = int(input("\nEnter a number to determine all factors of that number: "))
    print("\nFactors of",user_input,"are:")

    # printing the numbers if they are divisible and then storing it in the list
    for i in range(1, user_input + 1):
        if user_input % i == 0:
            print("\t",i)
            factors.append(i)
    
    # showing the summary
    print("\nIn Summary: ")
    no_of_factors = len(factors)

    for i in range( 0, no_of_factors // 2 ):
        print(factors[i],'*',factors[no_of_factors - i - 1],"=",user_input)

    # displaying the mid factor in the factors list since it didn't get included in the for loop above
    if no_of_factors % 2 != 0:
        print(factors[(no_of_factors//2) + 1],'*',factors[(no_of_factors//2) + 1],"=",user_input)

    # ask the user to continue or not?
    choice = input("Run again (y/n): ")
    if choice.startswith('n'):
        rewind = False
        print("Thank you for using our program!\nGood day to you!")
    elif choice.startswith('y'):
        factors = []
    else:
        rewind = False
        print("We couldn't understand that but we will terminate the program!\nGood day to you!")
