import random

# creating a class for the creature
class Creature():

    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.boredom = 0
        
        self.food = 2
        self.is_alive = True
        self.is_sleeping = False
    
    def eat(self):
        # simulating eating for the creature
        if self.food:
            self.food -= 1
            self.hunger -= random.randint(1,4)
            if self.hunger < 0:
                self.hunger = 0
            print(self.name,"ate a great meal today!")
        else:
            print(self.name,"has no food left!")
    
    def play(self):
        # simulate playing with the user
        print("\n",self.name,"wants to play a game with you!\n",self.name,"is thinking of a number between 0-2!")
        actual = random.randint(0,2)
        guess = int(input("What's your guess (0, 1, 2): "))
        if guess == actual:
            print("\nWow! You guessed it!",self.name,"had a lot of fun.")
            self.boredom -= 3
        else:
            print("\nOops! You couldn't guess it!",self.name,"was thinking of the number",actual)
            self.boredom -= 1
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        # simulate sleeping for the creature
        if self.is_sleeping:
            print("\nSssssshhhhhhhhhh......\n",self.name,"is already asleep!")
        else:
            self.is_sleeping = True
            print(self.name,"is now sleeping!\nZzzzz... Zzzzzzz... Zzzzz...")
            self.boredom -= 3
            self.tiredness -= 2
            if self.boredom < 0:
                self.boredom = 0
            if self.tiredness < 0:
                self.tiredness = 0

    def awake(self):
        # simulate waking the creature up
        if self.is_sleeping:
            actual = random.randint(0,2)
            if actual == 0:
                print("\n",self.name,"just woke up!")
                self.is_sleeping = False
                self.boredom = 0
            else:
                print("\n",self.name,"won't wake up!")
                self.boredom -= 3
                self.tiredness -= 2
                if self.boredom < 0:
                    self.boredom = 0
                if self.tiredness < 0:
                    self.tiredness = 0
    
    def clean(self):
        # simulate bathing
        self.dirtiness = 0
        print("\n",self.name,"just took a bath!")

    def forage(self):
        # simulate foraging for food
        found_food = random.randint(0,4)
        self.food += found_food
        self.dirtiness += 2
        print("\n",self.name,"found",found_food,"food pieces!")
    
    def show_values(self):
        # showing the details
        print('\nCreature Name:',self.name)
        print('Hunger(0-10):',self.hunger)
        print('Boredom(0-10):',self.boredom)
        print('Tiredness(0-10):',self.tiredness)
        print('Dirtiness(0-10):',self.dirtiness)
        print("\nFood Inventory:",self.food)
        if self.is_sleeping:
            status = 'Sleeping'
        else:
            status = 'Awake'
        print("Current Status:",status)

    def increment_values(self, difficulty):
        # increasing the difficulty
        self.hunger += random.randint(0, difficulty)
        self.dirtiness += random.randint(0, difficulty)
        if not self.is_sleeping:
            self.boredom += random.randint(0, difficulty)
            self.tiredness += random.randint(0, difficulty)
        
    def kill(self):
        if self.hunger >= 10:
            print("\n",self.name,"just starved to death!")
            self.is_alive = False
        elif self.dirtiness >= 10:
            print("\n",self.name,"suffered an infection and died!")
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            self.is_sleeping = False
            self.sleep()
            print("\n",self.name,"is bored and is sleeping!")
        elif self.tiredness >= 10:
            self.tiredness = 10
            self.is_sleeping = False
            self.sleep()
            print("\n",self.name,"is tired and is sleeping!")


# defining a function to show menu
def show_menu(creature):
    if creature.is_sleeping:
        input(f"Press any key to wake {creature.name} up!")
        creature.awake()
    else:
        print("\nEnter (1) to eat")
        print("Enter (2) to play")
        print("Enter (3) to sleep")
        print("Enter (4) to take a bath")
        print("Enter (5) to forage for food")
        choice = int(input("Enter your choice: "))
        return choice

def call_action( creature, action ):
    if action == 1:
        creature.eat()
    elif action == 2:
        creature.play()
    elif action == 3:
        creature.sleep()
    elif action == 4:
        creature.clean()
    elif action == 5:
        creature.forage()
    elif action == 6:
        creature.sleep()
    else:
        print("\nThat is an invalid option!")

print("Welcome to the Pythonagachi Simulator App!")

# creating a round var to keep track of rounds
rounds = 1

# creating a flag to exit the while loop
playing = True

# real game starts here

# taking basic user info
diff = int(input("Please choose a difficulty level (1-5): "))
if diff > 5:
    diff = 5
elif diff < 1:
    diff = 1
else: pass
name = input("What name would you like to give your pet Pythonogachi: ").title()

# creating creature
pet = Creature(name)

while playing:
    # displaying the rounds
    print("----------------------------------------------------------------------------")
    print("Round #",rounds)

    # showing menu and calling an action
    pet.show_values()
    result = show_menu( pet )
    if result:
        call_action( pet, result )
    print("\n\nRound #",rounds,"Summary: ")
    pet.show_values()

    # adding the spice of difficulty set by user
    pet.increment_values(diff)

    # checking if the creature has died or nah
    pet.kill()

    # stop game if creature died
    if not pet.is_alive:
        playing = False
        print("\nR.I.P\n",pet.name,"survived a total of",rounds,"rounds!")
        choice = input("Would you like to start over again (y/n): ")
        if choice.startswith('y'):
            pet = Creature(name)
            rounds = 1
            print("\nStarting over using the same game settings!\n")
        elif choice.startswith('n'):
            print("\nThank you for playing Pythonagachi!")
            playing = False
            break
        else:
            print("\nInvalid input! Thank you for playing Pythonagachi!")
            playing = False
            break
    else:
        rounds += 1

    input("Press any key to continue...")