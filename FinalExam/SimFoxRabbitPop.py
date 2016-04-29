import random
import numpy as np
import matplotlib.pyplot as plt

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    p_rabbit_reproduction = (1 - (CURRENTRABBITPOP/float(MAXRABBITPOP)))
    for rabbit in range(CURRENTRABBITPOP):
        if p_rabbit_reproduction > random.random():
            if CURRENTRABBITPOP < MAXRABBITPOP: #check to see max rabbit pop hasn't been exceeded
                CURRENTRABBITPOP += 1 #add rabbit

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    p_fox_eats_rabbits = (CURRENTRABBITPOP/float(MAXRABBITPOP))
    for fox in range(CURRENTFOXPOP):
        if p_fox_eats_rabbits > random.random() and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1 #sucessfully ate rabbit
            if 1.0/3.0 > random.random(): #will it reproduce?
                CURRENTFOXPOP += 1 #sucessfully gave birth
        else: #doesn't eat rabbit
            if 1.0/10.0 > random.random() and CURRENTFOXPOP > 10: #will it die?
                CURRENTFOXPOP -= 1 #it dies



def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for step in range(numSteps):
        if CURRENTFOXPOP < 10 or CURRENTRABBITPOP < 10:
            break
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

#plot - make function
x = range(200)
y = runSimulation(200)
labels = ["Rabit Population", "Fox Population"]
for y_arr, label in zip(y, labels):
    plt.plot(x, y_arr, label=label)
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.legend()
plt.show()


RP = y[0] #rabit population
FP = y[1] #fox population

#Fit polynomial lines of deg 2 Rabits
coeffRabbit = np.polyfit(range(len(RP)), RP, 2)
plt.plot(np.polyval(coeffRabbit, range(len(RP))))
plt.xlabel("Time Step")
plt.ylabel("Rabit Population")
plt.show()

#Fit polynomial lines of deg 2 Foxes
coeffFox = np.polyfit(range(len(FP)), FP, 2)
plt.plot(np.polyval(coeffFox, range(len(FP))))
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.show()

#Make function for bestfitlines
