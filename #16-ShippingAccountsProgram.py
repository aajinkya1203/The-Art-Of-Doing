print("Welcome to the Shipping Accounts Program!")

# creating a username list for 5 different person of my choice
username = ["aajinkya", "david", "jeff", "harry", "thomas"]

# take input to log into the account or nah
inputUsername = input("Hello, what is your username: ").lower().strip()

if inputUsername in username:

    # introductory message to the user
    print("Hello {}. Welcome back to your account.\nCurrent shipping prices are as follows:".format(inputUsername))
    print("\n\nShipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    # asking for the amount of samples
    item_no = int(input("How many items would you like to ship: "))
    rate = 0
    # setting the rate
    if item_no < 100:
        rate = 5.10
    elif item_no < 500:
        rate = 5.0
    elif item_no < 1000:
        rate = 4.95
    else:
        rate = 4.8
    
    print(f"To ship {item_no} items it will cost you ${ round( rate*item_no, 2) } at ${rate} per item")

    # taking confirmation from the user
    confirm = input("Would you like to place the order (y/n): ")
    if confirm.startswith('y'):
        print("Okay, Shipping your {} items".format(item_no))
    elif confirm.startswith('n'):
        print("Okay, no order is being placed at this time")
    else:
        print("Invalid input!\nCancelling order!")
else:
    # printing a message if account doesn't exitst
    print("Sorry, you do not have an account with us!\n")