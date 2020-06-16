import random

print("------------Power Ball Simulator------------")

# variables to keep a track of white-balls and red-ball
white_balls = []
red_ball = 0

# variables to set the limit for choosing the white and red balls
limit_white = 0
limit_red = 0

# variable for generating the odds of the user winning a lottery!
odds = 0

# list to generate and store the wining numbers
winning_numbers = []

# a list to keep track of all the sold tickets
sold = []

# flag to map victory
won = False

# variable to store the interval of user buying tickets!
interval = 0

# setting a flag to jump out of the break
flag = True

while flag:
    # taking user input for the limits:
    limit_white = int(input('How many white-balls to draw from for the 5 winning numbers (Normally 69):'))
    limit_red = int(input('How many red-balls to draw from for the Power-Ball (Normally 26):'))

    if limit_white <= 5:
        limit_white = 5
    else:
        pass
    
    if limit_red <= 1:
        limit_red = 1

    # generating odds of winning
    numerator = 0 + limit_white
    for i in range(1,5):
        numerator *= (limit_white - i)
    odds = (numerator * limit_red) / 120
    print("You have 1 in",odds,'chance of winning this lottery!')

    # taking input for the interval variable
    interval= int(input("Purchase tickets in what interval: "))

    # generating winning numbers
    list_white = list(range( 1, limit_white + 1 ))
    list_red = list(range( 1, limit_red + 1 ))
    # appending the random white nums
    for i in range(5):
        temp = random.choice( list_white )
        list_white.remove(temp)
        winning_numbers.append(temp)
    
    # sorting all the white nums and appending the red num
    winning_numbers.sort()
    winning_numbers.append( random.choice( list_red ) )

    # real game starts here
    print("------------Welcome to the Power-Ball------------")
    print("\nTonight's winning numbers are:",end='')
    for nums in winning_numbers:
        print(nums,end=" ")

    input("\nPress any key to begin purchasing tickets!")

    iterate = 0
    while iterate < interval:
        # generating the possible numbes into a list so that no duplication happens
        ticket_list_white = list(range( 1, limit_white + 1 ))
        ticket_list_red = list(range( 1, limit_red + 1 ))
        my_ticket = []

        for i in range(5):
            tempo = random.choice( ticket_list_white )
            ticket_list_white.remove(tempo)
            my_ticket.append(tempo)
        
        # sorting all the white nums and appending the red num
        my_ticket.sort()
        my_ticket.append( random.choice( ticket_list_red ) )

        # disregarding the ticket if it's already been bought!
        if my_ticket in sold:
            print("Sold ticket generated again!\nDisregarding the ticket...")
            continue

        # appending all the tickets to sold list
        sold.append( my_ticket )

        # printing this ticket
        print( my_ticket ) 

        if my_ticket == winning_numbers:
            print("\nWinning ticket numbers are:",end='')
            for nums in winning_numbers:
                print(nums,end=" ")
            print("\n\nCongratulations! You've won the Power Ball!")
            print("\nYou've purchased a total of {} tickets".format( len(sold) ))
            won = True
            flag = False
            break
        else:
            if iterate+1 == interval:
                print(len(sold),"tickets purchased so far with no winners!")
                choice = input("\nKeep Purchasing (y/n): ")
                if choice.startswith('y'):
                    iterate = 0
                    continue
                else:
                    flag = False
        iterate += 1


if won == False:
    print(f"You bought {len(sold)} tickets and still lost!\nBetter luck next time!")