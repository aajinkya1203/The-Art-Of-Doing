import random
import math
import tkinter as tk
# all class definitions up here
class Simulation():
    def __init__(self):
        self.day_number = 1
        # taking input for the population
        print("\nTo simulate an epidemic outbreak, we must know the population size.")
        self.population_size = abs(int(input("---Enter the population size:")))

        root = math.sqrt(self.population_size)
        if int(root +.5)**2 != self.population_size:
            # is not a perf squre
            root = round(root, 0)
            # grid size for the gui
            self.grid_size = int(root)
            # setting the population size = grid**2
            self.population_size = self.grid_size ** 2
            print("\nThe simulation is rounding the population to", self.population_size,"for visual purposes!\n")
        else:
            # is a perfect sq
            self.grid_size = int(math.sqrt(self.population_size))

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
        # this list will be a 2D list
        self.population = []
        for i in range( simulation.grid_size ):
            row = []
            for i in range( simulation.grid_size ):
                # creating that many person - populating
                person = Person()
                row.append( person )
            # appending a list of N people as a row in the population list
            self.population.append( row )

    def initial_infection(self, simulation):
        # no of people who must start infected acc. to their condition (casting it into an int var)
        infected_count = int(round(simulation.infection_percent * simulation.population_size, 0))
        # infecting that many people in the population
        infections = 0
        while infections < infected_count:
            x = random.randint( 0, simulation.grid_size-1 )
            y = random.randint( 0, simulation.grid_size-1 )
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
            infections += 1

    def spread_infection(self, simulation):
        # simulating the spread of the infection
        # an infection spread if the people around you are infected, so
        # for loop for rows
        for i in range( simulation.grid_size ):
            # for loops for columns
            for j in range( simulation.grid_size ):
                # if the person is alive
                if not self.population[i][j].is_dead:
                    # different conditions
                    # first row
                    if i == 0:
                        if j == 0:
                            # first person in the grid, check right or down
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == (simulation.grid_size - 1):
                            # last person in the first row, check left or dowm
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            # person in first row but in middle, check for left, right or down
                            if self.population[i][j+1].is_infected or self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    # checking the last row
                    elif i == (simulation.grid_size - 1):
                        if j == 0:
                            # first person in the last row, check right or up
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == (simulation.grid_size - 1):
                            # last person in the last row, check left or up
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            # person in last row but in middle, check for left, right or up
                            if self.population[i][j+1].is_infected or self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    elif i < (simulation.grid_size - 1):
                        # middle rows
                        if j == 0:
                            # first person in the row, check right or up or down
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == (simulation.grid_size - 1):
                            # last person in the row, check left or up or down
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            # person in the row but in middle, check for left, right or up or down
                            if self.population[i][j+1].is_infected or self.population[i][j-1].is_infected or self.population[i-1][j].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

    def update(self, simulation):
        # updating the parameters of the simulation
        simulation.day_number += 1
        for i in self.population:
            for j in i:
                j.update(simulation)
    
    def display_statistics(self,simulation):
        # counting the number of people affected
        total_infected_count = 0
        total_death_count = 0
        for persons in self.population:
            for person in persons:
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


# function for graphics - note this is not part of any class
def graphics(simulation, population, canvas):
    # for the canvas
    # using floor division to set the sq dimension
    square_dimension = 600 // simulation.grid_size

    for i in range(simulation.grid_size):
        # y loc of person
        y = i*square_dimension
        for j in range(simulation.grid_size):
            # x loc of person
            x = j*square_dimension
            if population.population[i][j].is_dead:
                # person is dead
                # draw red square
                canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill="red")
            else:
                if population.population[i][j].is_infected:
                    # person infected, draw yellow square
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill="Yellow")
                else:
                    # person is healthy, green square
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill="green")
                

print("Welcome to the Epidemic Outbreak GUI App!")

# real simulation starts here


# setting some constants 
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

# creating a tkinter window and a canvas and giving a title
sim_window = tk.Tk()
sim_window.title("Epidemic Outbreak")
# canvas obj
sim_canvas = tk.Canvas(sim_window, width=WINDOW_WIDTH, height = WINDOW_HEIGHT, bg="lightblue" )
sim_canvas.pack(side = tk.LEFT)

# creating a simulation obj
simulation = Simulation()
# creating a Population obj
population = Population(simulation)

# initial infection wave
population.initial_infection(simulation)

# displaying stats
population.display_statistics(simulation)

# displaying the status of people's condition
# graphics(simulation, population, sim_canvas)

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
    graphics(simulation, population, sim_canvas)

    # updating the window
    sim_window.update()

    if i != simulation.sim_day- 1:
        # prompt the user to press enter for next day's simulation
        input("\nPress ENTER for next day's simulation...")
        # deleting all today's canvas
        sim_canvas.delete("all")