print("Welcome to the Even Odd Number Sorter App!")

# using a list to store all the even and odd numbers
even = []
odd = []

# setting a flag to break out of the while loop
redo = True

# process starts here
while redo:
    user_string = input("Enter in a string of numbers separated by a comma (,) : ")
    new_list = user_string.replace(" ","")
    new_list = new_list.split(',')

    print("Summary!")
    for number in new_list:
        number = int(number)
        if number % 2 == 0:
            print("\t",number,"is even!")
            even.append(number)
        else:
            print("\t",number,"is odd!")
            odd.append(number)
    # sorting the lists
    even.sort()
    odd.sort()
    # displaying all the numbers that are even and then all those who are odd
    print("Following {} are even numbers:\tFollowing {} are odd numbers".format(len(even),len(odd)))
    for eve, od in zip(even, odd):
        print(eve,"\t\t\t\t\t",od)

    choice = input("Would you like to go again (y/n): ")
    if choice.startswith('n'):
        redo = False
        print("Thank you for using our program!\nGood day to you!")
    even = []
    odd = []