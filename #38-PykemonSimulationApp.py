import random
# all class definitions here
class Pykemon():
    def __init__(self, name, element, health, speed):
        self.name = name
        self.element = element
        self.max_health = health
        self.current_health = health
        self.speed = speed
        self.is_alive = True
        self.moves = []

    def light_attack(self, enemy):
        damage = random.randint(15, 25)
        print("\n\n",self.name, 'used', self.moves[0])
        print("Damage dealt to the enemy:",damage)
        enemy.current_health -= damage
    
    def heavy_attack(self, enemy):
        damage = random.randint(0, 50)
        print("\n\n",self.name, 'used', self.moves[1])
        if damage < 10:
            print("\nOh no!",self.name,"missed the attack!\nNo damage dealt.")
        else:
            print("Damage dealt to the enemy:",damage)
            enemy.current_health -= damage
    
    def restore(self):
        heal = random.randint(15, 25)
        print("\n\n",self.name, 'used', self.moves[2])
        print(self.name,"restored",heal,"points!")
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health
    
    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print(self.name,"has fainted!")
            input("Press any key to continue...")
    
    def show_stats(self):
        print("\n\nPykemon's Name:",self.name)
        print("Element:",self.element)
        print("Current Health:",self.current_health)
        print("Max Health:",self.max_health)
        print("Speed:",self.speed)
    
class Fire(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name,element,health,speed)
        self.moves = [ 'Scratch', 'Ember', 'Light', 'Fire Blast' ]

    def special_attack(self, enemy):
        print("\n\n",self.name, 'used', self.moves[3])
        if enemy.element == "GRASS":
            print("\nThat was a super effective move!")
            damage = random.randint(35, 50)
        elif enemy.element == "WATER":
            print("\nThat was not an effective move!")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print("Damage dealt to the enemy:",damage)
        enemy.current_health -= damage

    def move_info(self):
        print(self.name,"moves:\n")
        print(f"--{ self.moves[0] }--")
        print("\tAn efficient attack...\n\tGuaranteed to do damage within the range of 15 to 25 damage points.")
        print(f"--{ self.moves[1] }--")
        print("\tA risky attack...\n\tCould deal up to 50 damage points or as little as 0 damage points.")
        print(f"--{ self.moves[2] }--")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points.")
        print(f"--{ self.moves[3] }--")
        print("\tA powerful FIRE based attack...\n\tGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")

class Water(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name,element,health,speed)
        self.moves = [ 'Bite', 'Splash', 'Dive', 'Water Cannon' ]

    def special_attack(self, enemy):
        print("\n\n",self.name, 'used', self.moves[3])
        if enemy.element == "FIRE":
            print("\nThat was a super effective move!")
            damage = random.randint(35, 50)
        elif enemy.element == "GRASS":
            print("\nThat was not an effective move!")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 20)
        print("Damage dealt to the enemy:",damage)
        enemy.current_health -= damage

    def move_info(self):
        print(self.name,"moves:\n")
        print(f"--{ self.moves[0] }--")
        print("\tAn efficient attack...\n\tGuaranteed to do damage within the range of 15 to 25 damage points.")
        print(f"--{ self.moves[1] }--")
        print("\tA risky attack...\n\tCould deal up to 50 damage points or as little as 0 damage points.")
        print(f"--{ self.moves[2] }--")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points.")
        print(f"--{ self.moves[3] }--")
        print("\tA powerful FIRE based attack...\n\tGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")

class Grass(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name,element,health,speed)
        self.moves = [ 'Vine Whip', 'Wrap', 'Grow', 'Leaf Blade' ]

    def special_attack(self, enemy):
        print("\n\n",self.name, 'used', self.moves[3])
        if enemy.element == "WATER":
            print("\nThat was a super effective move!")
            damage = random.randint(35, 50)
        elif enemy.element == "FIRE":
            print("\nThat was not an effective move!")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 20)
        print("Damage dealt to the enemy:",damage)
        enemy.current_health -= damage

    def move_info(self):
        print(self.name,"moves:\n")
        print(f"--{ self.moves[0] }--")
        print("\tAn efficient attack...\n\tGuaranteed to do damage within the range of 15 to 25 damage points.")
        print(f"--{ self.moves[1] }--")
        print("\tA risky attack...\n\tCould deal up to 50 damage points or as little as 0 damage points.")
        print(f"--{ self.moves[2] }--")
        print("\tA restorative move...\n\tGuaranteed to heal your Pykemon 15 to 25 health points.")
        print(f"--{ self.moves[3] }--")
        print("\tA powerful FIRE based attack...\n\tGuaranteed to deal MASSIVE damage to WATER type Pykemon.")

class Game():
    def __init__(self):
        # list of possible pykemon elements
        self.pykemon_elements = [ 'FIRE', "WATER", "GRASS" ]
        # list of possible pykemon names
        self.pykemon_name = [ 'Chewdie', 'Spatol','Burnmander', 'Pykachu', 
        'Pyonx', 'Abbacab', 'Sweetil', 'Jampot','Hownstooth', 'Swagilybo', 'Muttle',
        'Zantbat', 'Wiggly Poof', 'Rubblesaur' ]
        # keeps a track of the number of battles won
        self.battles_won = 0

    def create_pykemon(self):
        # creating a pykemon with the props settings selected randomly
        health = random.randint(70,100)
        speed = random.randint(1,10)
        element = random.choice( self.pykemon_elements )
        name = random.choice( self.pykemon_name )
        if element == "FIRE":
            my_pyke = Fire( name, element, health, speed )
        elif element == "WATER":
            my_pyke = Water( name, element, health, speed )
        else:
            my_pyke = Grass( name, element, health, speed )
        
        # returning the created pykemon
        return my_pyke

    def choose_pykemon(self):
        starters = []
        # choosing the starting 3 pokemons
        while len(starters) < 3:
            temp = self.create_pykemon()
            valid_pykemon = True
            for starter in starters:
                if starter.name == temp.name or starter.element == temp.element:
                    valid_pykemon = False
            if valid_pykemon:
                starters.append( temp )

        for starter in starters:
            starter.show_stats()
            print("\n\n")
            starter.move_info()

        # asking the user which pykemon to select
        print("\nProfessor Aajinkya presents you with three Pykemon: ")
        for i, starter in enumerate(starters):
            print(f"({i+1}) - {starter.name}")
        choice=int(input("Which Pykemon would you like to choose: "))
        if choice == 1:
            return starters[0]
        elif choice == 2:
            return starters[1]
        elif choice == 3:
            return starters[2]
        else:
            print("\nInvalid choice! Let us select for you then...")
            index = random.randint(0,2)
            return starters[index]

    def get_attack(self, player):
        # asking the user what move would they like to move->
        print("\n\nChoose an Attack:")
        for index, attack in enumerate(player.moves):
            print(f"({index+1}) - {attack}")
        choice = int(input("Enter your choice: "))
        print("\n------------------------------------------")
        if choice > 4 or choice < 1:
            print("\nInvalid input! We will choose for you!")
            choice = random.randint(1, 4)
        return choice
    
    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        else:
            player.special_attack(computer)
        computer.faint()

    def computer_attack(self, player, computer):
        move = random.randint(1, 4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        else:
            computer.special_attack(player)
        player.faint()

    def battle(self, player, computer):
        # simulating battle
        move = self.get_attack(player)
        if player.speed >= computer.speed:
            self.player_attack(move, player, computer)
            if computer.is_alive:
                self.computer_attack(player, computer)
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)

# some cheesy intro messages
print("Welcome to the Pykemon Simulation App!")
print("Can you become the worlds greatest Pykemon Trainer?!")
print("\n\nDon't worry! Prof Aajinkya is here to help you on your quest.")
print("He would like to gift you your first Pykemon!")
print("Here are three potential Pykemon partners.")
input("Press any key to choose your Pykemon!")

# main game starts here - compiling all the functions

# setting a flag to help exit the while loop
playing = True

while playing:
    # creating a game obj
    game = Game()

    # allowing the user to choose the pykemon
    pykemon = game.choose_pykemon()
    print("\nCongratulations Trainer, you have chosen", pykemon.name,'!')
    input("\nYour journey with Spatol beings now...Press ANY KEY")

    # creating enemy and battling
    while pykemon.is_alive:
        enemy = game.create_pykemon()
        print("\nOh no! A wild {} has appeared!".format(enemy.name))
        enemy.show_stats()

        # battle startttssss!!!!
        while pykemon.is_alive and enemy.is_alive:
            game.battle(pykemon, enemy)
            if pykemon.is_alive and enemy.is_alive:
                pykemon.show_stats()
                enemy.show_stats()
                print("\n--------------------------------------------------------------------------------\n")
        if pykemon.is_alive:
            game.battles_won += 1

    # player is dead
    print(pykemon.name,"has fainted!")
    print("But not before defeating {} Pykemons!".format(game.battles_won))

    # play again?
    again = input("Would you like to play again (y/n):")
    if again.startswith('y'):
        pass
    elif again.startswith('n'):
        playing = False
        print("\nThanks for playing Pykemon Simulation!")
    else:
        print("\nInvalid Input, but we will consider it as a no!")
        playing = False
        print("\nThanks for playing Pykemon Simulation!")


