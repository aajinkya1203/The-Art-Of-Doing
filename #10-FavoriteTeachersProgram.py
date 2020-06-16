print("Welcome to the Favorite Teachers Program!")

# a list to keep track of all teachers!
fav = []
fav.append(input("Who is your first favourite teacher: ").title())
fav.append(input("Who is your second favourite teacher: ").title())
fav.append(input("Who is your third favourite teacher: ").title())
fav.append(input("Who is your fourth favourite teacher: ").title())

# creating a funtion to print the details after every update to the list
def showSummary(teachers):
    print("\nYour favourite teachers ranked are:",teachers)
    print("\nYour favourite teachers alphabetically are:",sorted(teachers))
    print("\nYour favourite teachers in reverse alphabetical order are:",sorted(teachers, reverse=True))
    print("\n\nYour top two teachers are {} and {}".format(teachers[0], teachers[1]))
    print("\nYour next two teachers are {} and {}".format(teachers[2], teachers[3]))
    print("\nYour leat favourite teacher is",teachers[-1])
    print("\nYou have a total of {} favourite teachers".format(len(teachers)))

# showing the details and adding a new fav teacher
showSummary(fav)
print(f"Oops,{fav[0]} is no longer your first favourite teacher!")
fav.insert(0, input("Who is your new first favouurite teacher: ").title())

# removing the non-fav teacher
print("\nYou've decided you no longer have a favourite teacher!\n")
to_remove = input("Which teacher would you like to remove from you list: ").title()
fav.remove(to_remove)
showSummary(fav)