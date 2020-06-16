import datetime as dt
print("Welcome to the Grocery List App!")

# creating an object of dt and displaying the date in the format mm/dd hh:mm
date = dt.datetime.now()
hour = date.hour
minute = date.minute
month = date.month
day = date.day

print(f"Current Date and Time: {month}/{day} {hour}:{minute}\n")

# current cart items
cart = [ "Meat", "Cheese" ]
print("You currently have {} and {} in your shopping list!".format(cart[0], cart[1]))

# taking user input for 3 times
cart.append(input("Type of food to add to your list: ").title())
cart.append(input("Type of food to add to your list: ").title())
cart.append(input("Type of food to add to your list: ").title())

# displaying the updated list
print("\n\nHere is your grocery list:\n",cart)
cart.sort()
print("\n\nHere is your grocery list sorted:\n",cart)

# shopping process
print("Simulating Shopping Process...")

# using a for loop to repeat the process 3 times as per the question
for i in range(0, 3):

    print("\nCurrent grocery list: {} items".format(len(cart)),"\n",cart)

    # removing the items bought by the user from the list
    temp = input("What food did you just buy: ").title()
    cart.remove(temp)

print("\n\nCurrent grocery list: {} items".format(len(cart)),"\n",cart)

# informing the user that the store doesn't have one of the items in the cart
print("\nSorry, the store is out of {}".format(cart.pop()))

# asking for replacement to that item
cart.append(input("\nWhat food would you like instead: ").title())

# displaying the final 2 items in the list in a sorted manner
cart.sort()
print("\n\nHere is what remains on your list:\n",cart)