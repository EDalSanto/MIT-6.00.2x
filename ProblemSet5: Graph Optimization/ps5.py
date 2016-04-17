
# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#


import string
from graph import *
# This imports everything from `graph.py` as if it was defined in this file!


#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here
# describing how you will model this problem as a graph.

### each building will be represented by a node
    #the first two columns in mit_map.txt represent buldings with an edge, that are connected
        #column 1 will be the src, column 2 the dest
### each edge has a total distance(3rd column) and outdoor distance(4th)

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    g = WeightedDigraph()
    print "Loading map from file..."
    with open(mapFilename) as inputfile:
        for line in inputfile:
            try:
                src = Node(line.split()[0])
                g.addNode(src)
            except ValueError:
                pass
            try:
                dest = Node(line.split()[1])
                g.addNode(dest)
            except ValueError:
                pass
            g.addEdge(WeightedEdge(src, dest, line.split()[2], line.split()[3]))
    return g

mitMap = load_map("mit_map.txt")
# #print mitMap
# print mitMap.nodes
# print mitMap.edges
# print isinstance(mitMap, Digraph) #True
# print isinstance(mitMap, WeightedDigraph) #True


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
# minimzing TotalDistance between two nodes which will be sum of edges TotalDistance, which we can access with edge.getTotalDistance.
#constraints are TotalDistance can not exceed maxTotalDist, and the distance spent outdoors can not exceed maxDistOutdoors
#
def printPath(path):
    result = ''
    for node in path:
        result = result + str(node) + '>'
    return result[:-1]

# print printPath([1,2,3])
# print "enumerated path: ", enumerate(printPath([1,2,3]))

paths = []

def refreshPaths():
    global paths
    paths = []

def genPaths(digraph, start, end, path = []):
    '''
    generates successful_paths from start to end
    '''
    path = path + [start]
    if start == end:
        paths.append(path)
    for node in digraph.childrenOf(start):
        if node not in path:
            genPaths(digraph, node, end, path)

def satisfyConstraints(paths, digraph, maxTotalDist, maxDistOutdoors):
    '''
    finds paths that satisfy constrains and have lowest cost
    '''
    constraint_satisfying_paths = []
    for path in paths:
        total_outdoors = 0.0
        total_dist = 0.0
        for index, node in enumerate(path[:-1]): #skip last node which won't have children
            children_of_node = digraph.childrenOf(node)
            for child in children_of_node:
                if child == path[index + 1]: #means that they're connected
                    for dest in digraph.edges[node]:
                        if dest[0] == child:
                            total_outdoors += dest[1][1]
                            total_dist += dest[1][0]
        if total_outdoors <= maxDistOutdoors and total_dist <= maxTotalDist:
            constraint_satisfying_paths.append([path, total_dist])
    return constraint_satisfying_paths

 #satisfyDistOutDoors(paths, digraph, maxDistOutdoors)

def shortestPath(constraint_satisfying_paths):
    '''returns shortest length path of paths that meet constraints of not exceeding maxTotalDist and maxDistOutdoors
    '''
    if constraint_satisfying_paths == []:
        return []
    else:
        min = constraint_satisfying_paths[0][1] #start with 0th path as min cost
        shortest_path = constraint_satisfying_paths[0][0]
        for path, dist in constraint_satisfying_paths[1:]:
            if dist <= min:
                min = dist
                shortest_path = path
        return shortest_path
# print shortestPath(paths)


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    genPaths(digraph, Node(start), Node(end), path = [])
    constraint_satisfying_paths = satisfyConstraints(paths, digraph, maxTotalDist, maxDistOutdoors)
    shortest_path = [str(elm) for elm in shortestPath(   constraint_satisfying_paths)]
    refreshPaths()
    if shortest_path == []:
        raise ValueError("No such path!")
    return shortest_path
