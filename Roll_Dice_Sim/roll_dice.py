import random

def rollDie():
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

#print rollN(5)

def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries += 1
        result = rollN(numRolls)
        if result == goal:
            return numTries

#print getTarget('11')
#How long 1 simulation takes to get target i.e, '11' when rolling 2 dice

def runSim(goal, numTrials):
    total = 0
    for i in range(numTrials):
        total += getTarget(goal)
    print 'Average number of tries =', total/float(numTrials)

#print runSim('11111', 100)
#print runSim('54324', 100)
#how long takes to achieve goal over a defined number of trials, NumTrials

def atLeastOneOne(goal, numRolls, numTrials):
    numSuccess = 0
    for i in range(numTrials):
        rolls = rollN(numRolls)
        if goal in rolls:
            numSuccess += 1
        fracSuccess = numSuccess/float(numTrials)
    print fracSuccess

#print atLeastOneOne('1', 10, 1000)
#calculates % of succesful outcomes for a given user-defined goal, a number of rolls(NumRolls, and a number of trials(NumTrials)