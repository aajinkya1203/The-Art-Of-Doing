import random
# all class definitions up here
class Simulation():
    def __init__(self):
        self.day_number = 1
        # taking input for the population
        print("\nTo simulate an epidemic outbreak, we must know the population size.")
        self.population_size = abs(int(input("---Enter the population size:")))
        # % of population already infected
        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = float(input("--Enter the percentage (0-100) of the population to initially infect: "))
        self.infection_percent /= 100
        # risk to a person due to the pandemic
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("--Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        self.infection_probability /= 100
        # duration of infection - estimate
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input('--Enter the duration (in days) of the infection:'))
        # mortality rate of those already infected by the diesease
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("--Enter the mortality rate (0-100) of the infection:"))
        # simulation to be run for how many days
        print("\nWe must know how long to run the simulation.")
        self.sim_day = int(input('--Enter the number of days to simulate:'))

# class Person starts here
class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0
    
    def infect(self, simulation):
        # simulate a person getting infected
        chance_of_infection = random.randint(0, 100)
        if chance_of_infection < simulation.infection_probability:
            # infecting the person
            self.is_infected = True
    
    def heal(self):
        # simulate an infected person healing up
        self.is_infected = False
        self.days_infected = 0
    
    def die(self):
        # simulate a person dying due to the pandemic
        self.is_dead = True


    def update(self,simulation):
        # updating the parameters of the person
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                chances = random.randint(0, 100)
                if chances < simulation.mortality_rate:
                    # person couldn't survive
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()
    
# Population class
class Population():
    def __init__(self, simulation):
        self.population = []
        for i in range( simulation.population_size ):
            # creating that many person - populating
            person = Person()
            self.population.append( person )

    def initial_infection(self, simulation):
        # no of people who must start infected acc. to their condition (casting it into an int var)
        infected_count = int(round(simulation.infection_percent * simulation.population_size, 0))
        # infecting that many people in the population
        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
        
        # shuffling the list so that it is more realistic
        random.shuffle( self.population )

    def spread_infection(self, simulation):
        # simulating the spread of the infection
        # an infection spread if the people around you are infected, so
        for i in range( len( self.population ) ):
            # if the person is alive
            if not self.population[i].is_dead:
                # different conditions
                if i == 0 and self.population[i+1].is_infected:
                    self.population[i].infect(simulation)
                elif i < (len(self.population)-1):
                    if self.population[i-1].is_infected or self.population[i+1].is_infected:
                        self.population[i].infect(simulation)
                elif i == len(self.population)-1 and self.population[i-1].is_infected:
                    self.population[i].infect(simulation)
    
    def update(self, simulation):
        # updating the parameters of the simulation
        simulation.day_number += 1
        for person in self.population:
            person.update(simulation)
    
    def display_statistics(self,simulation):
        # counting the number of people affected
        total_infected_count = 0
        total_death_count = 0
        for person in self.population:
            if person.is_infected:
                total_infected_count += 1
                if  person.is_dead:
                    total_death_count += 1
            
        infected_percent = round( ( 100 * (total_infected_count/len(self.population)) ) ,4)
        death_percent = round( ( 100 * (total_death_count/len(self.population)) ) ,4)
        # printing stats of the day
        print(f"\n\n----Day #{simulation.day_number}----")
        print(f"Percentage of Population Infected: {infected_percent}")
        print(f"Percentage of Population Dead: {death_percent}")
        print(f"Total People Infected: {total_infected_count}/{len(self.population)}")
        print(f"Total Deaths: {total_death_count}/{len(self.population)}")
        input("Press Enter to advance to the next day:")

    def graphics(self):
        status = []
        # adding each person's status acc.to their condition into the list
        for person in self.population:
            if person.is_dead:
                char = 'X'
            else:
                if person.is_infected:
                    char = 'I'
                else:
                    char = 'O'
            status.append(char)
        # printing the status
        print("\nStatus:\nO - Alive\tI - Infected\tX - Dead\n")
        for stat in status:
            print(stat, end='-')
        
                

print("Welcome to the Epidemic Outbreak Terminal App!")

# real simulation starts here

# creating a simulation obj
simulation = Simulation()
# creating a Population obj
population = Population(simulation)

# initial infection wave
population.initial_infection(simulation)

# displaying stats
population.display_statistics(simulation)

# displaying the status of people's condition
population.graphics()

input("\nPress ENTER to being the simulation...")

# each day simulation
for i in range(1,simulation.sim_day):
    # spreading the infection first
    population.spread_infection(simulation)

    # updating the population
    population.update(simulation)

    # displaying current day's stats
    population.display_statistics(simulation)
    # showing current day's graphics
    population.graphics()

    if i != simulation.sim_day- 1:
        # prompt the user to press enter for next day's simulation
        input("\nPress ENTER for next day's simulation...")