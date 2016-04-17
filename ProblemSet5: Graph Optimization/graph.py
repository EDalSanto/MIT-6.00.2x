# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight1, weight2):
        Edge.__init__(self, src, dest)
        self.weight1 = weight1
        self.weight2 = weight2
    def getTotalDistance(self):
        return self.weight1
    def getOutdoorDistance(self):
        return self.weight2
    def __str__(self):
        return '{0}->{1} ({:d}, {:d})'.format(self.src, self.dest, self.weight1, self.weight2)


class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self,node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError("No duplicate nodes")
        else:
            self.nodes.add(node) #adds node object to set of nodes
            self.edges[node] = []
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self,node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            #source nodes in edges not stored in any particular order
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

# g = Digraph()
# na = Node('a')
# nb = Node('b')
# nc = Node('c')
# g.addNode(nc)
# g.addNode(nb)
# g.addNode(na)
# e = Edge(na, nb)
# e1 = Edge(nb, nc)
# g.addEdge(e)
# g.addEdge(e1)
# print type(nb)
# print g.childrenOf(na)
# print g

class WeightedDigraph(Digraph):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest,(float(edge.getTotalDistance()),
        float(edge.getOutdoorDistance()))])
    def childrenOf(self,node):
        return [elm[0] for elm in self.edges[node]]
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{}{}->{} {}\n'.format(res, k, d[0], d[1])
        return res[:-1]

# nh = Node('h')
# nj = Node('j')
# nk = Node('k')
# nm = Node('m')
# ng = Node('g')
# g = WeightedDigraph()
# g.addNode(nh)
# g.addNode(nj)
# g.addNode(nk)
# g.addNode(nm)
# g.addNode(ng)
# randomEdge = WeightedEdge(nk, nm, 41, 23)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nh, nj, 27, 23)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nk, nh, 18, 11)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nm, nj, 56, 29)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nh, nj, 44, 15)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nm, nh, 35, 12)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nk, nh, 22, 22)
# g.addEdge(randomEdge)
# randomEdge = WeightedEdge(nm, nk, 67, 22)
# g.addEdge(randomEdge)
# print g.childrenOf(nh)
# print g.childrenOf(nj)
# print g.childrenOf(nk)
# print g.childrenOf(nm)
# print g.childrenOf(ng)
