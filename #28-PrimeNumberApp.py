# importing time to measure the time it takes to run the code
import time

print("Welcome to the Prime Number App")

# setting a flag which marks if the number is prime or not
not_prime = False

# setting a flag for the while loop
redo = True

# creating a function to check if a number is prime or not
def checkPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

# while loop starts
while redo:
    print("\nEnter 1 to determine if a specific number is prime.\nEnter 2 to determine all prime numbers within a set range.")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        user_number =int(input("Enter a number to determine if it is prime or not: "))
        not_prime = checkPrime( user_number )
        
        # showing a suitable mmessage if the number was prime
        if not_prime:
            print(user_number,"is not a prime number!")
        else:
            print(user_number,"is a prime number!")
    elif choice == 2:
        lower_bound = int(input("Enter the lower bound of your range: "))
        upper_bound = int(input("Enter the upper bound of your range: "))
        print("\nThe following numbers between",lower_bound,"and",upper_bound,"are prime: ")

        # marking start time
        time1 = time.time()

        for i in range( lower_bound, upper_bound+1 ):
            # checking prime condition for all numbers
            not_prime = checkPrime( i )
            # showing the number only if the number is prime
            if not_prime == False:
                print("\t",i)
        time2 = time.time() - time1
        print("Calculations took", round(time2, 4),"s")
    else:
        print("\nThat's an invalid input!")

    choice = input("\n\nWould you like to run the program again (y/n): ")
    if choice.startswith('n'):
        redo = False
        print("Thanks for using our program!")
    not_prime = False