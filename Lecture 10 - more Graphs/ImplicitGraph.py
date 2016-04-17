class puzzle(object):
    def __init__(self, order):
        self.label = order #gives order of puzzle
        for index in range(9):
            if order[index] == '0': #empty tile
                self.spot = index
                return None
    def transition(self, to):
        '''
        Creates edges
        to: the place to which we're going to do a shift
        '''
        label = self.label #inital order of puzzle
        blankLocation = self.spot #initial blank spot
        newBlankLabel = str(label[to])
        newLabel = '' #keeps track of new label aka state of puzzle created in for loop below
        for i in range(9):
            if i == to:
                newLabel += '0' #to becomes empty place
            elif i == blankLocation:
                newLabel += newBlankLabel #bl
            else:
                newLabel += str(label[i])
        return puzzle(newLabel)
    def __str__(self):
        return self.label



def DFSWithGeneratorShortest(start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    if start.label == end.label:
        return path
    for shift in shiftDict[start.spot]:
        new = start.transition(shift)
        if new.label not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFSWithGeneratorShortest(new,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFSWithGenerator(start, end, q = []):
    initPath = [start] #initial state of puzzle turned into list
    q.append(initPath) #queue data structure: first in, first out; list of lists(states)
    while len(q) != 0:
        tmpPath = q.pop(0) #pop off first elm(State) of queue first
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label: #if state of puzzle correct
            return tmpPath #we're done, return path
        for shift in shiftDict[lastNode.spot]: #for all possible shifts accessed from shiftDict
            new = lastNode.transition(shift) #creates new puzzle for each shift
            if notInPath(new, tmpPath): #makes sure state not already in path
                newPath = tmpPath + [new]
                q.append(newPath)
    return None

def DFSWithGenerator(start, end, stack = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    initPath = [start]
    stack.insert(0, initPath)
    while len(stack)!= 0:
        tmpPath = stack.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath): #avoid cycles
                newPath = tmpPath + [new]
                stack.insert(0, newPath)
    return None


def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True

'''
shiftDict represents all possible shifts if the empty tile is at a given location
'''

shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]

goal = puzzle('012345678')
test1 = puzzle('125638047')


def printGrid(pzl):
    data = pzl.label
    print data[0], data[1], data[2]
    print data[3], data[4], data[5]
    print data[6], data[7], data[8]
    print ''

def printSolution(path):
    for elt in path:
        printGrid(elt)

path = BFSWithGenerator(test1, goal)
print printSolution(path)
