import random


class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = [] #creates empty list(which is dict!)
        self.numBuckets = numBuckets #sets num of buckets, indice spaces in dictionary
        for i in range(numBuckets): #add bucket/indice spaces to our dict/list
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets] #finds bucket/(list) for key/value pair
        for i in range(len(hashBucket)): #if a tuple is already 
            if hashBucket[i][0] == dictKey: #if for ith element in that hashbucket the current key is equal to our new key
                hashBucket[i] = (dictKey, dictVal) #make that that ith element in the hashbucket our new key/value tuple
                return
        hashBucket.append((dictKey, dictVal)) #if nothing is already there, just append tupple
        
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets] #finds hashvalue for parameter key
        for e in hashBucket: #for every elm in that bucket
            if e[0] == dictKey: #if key found
                return e[1] #return value
        return None #otherwise return none
    
    def __str__(self):
        res = ''   #empty string
        for b in self.buckets: #for hashbuckets in dict
            for t in b: #for tuples in each hashbuckets
                res = res + str(t[0]) + ':' + str(t[1]) + ',' #res increased by pairs
        return '{' + res[:-1] + '}' # Change 2 #dict representation as seen externally 

def collision_prob(numBuckets, numInsertions):
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return 1 - prob

def max_class(p):
	"""
	calculates max class size to have a probability p that 2 people share a birthday
	"""
	import math
	max = math.sqrt(730*math.log(1/(1-p)))
	return max
		 
	
def sim_insertions(numBuckets, numInsertions):
    '''
    Run a simulation for numInsertions insertions into the hash table.
    '''
    choices = range(numBuckets)
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return False
        else:
            used.append(hashVal)
    return True

def observe_prob(numBuckets, numInsertions, numTrials):
    '''
    Given the number of buckets and the number of items to insert, 
    runs a simulation numTrials times to observe the probability of a collision.
    '''
    probs = []
    for t in range(numTrials):
        probs.append(sim_insertions(numBuckets, numInsertions))
    return 1 - sum(probs)/float(numTrials)


def main():
    hash_table = intDict(25)
    hash_table.addEntry(15, 'a')
#    random.seed(1) # Uncomment for consistent results
    for i in range(20):
       hash_table.addEntry(int(random.random() * (10 ** 9)), i)
    hash_table.addEntry(15, 'b')
    print hash_table.buckets  #evil
    print '\n', 'hash_table =', hash_table
    print hash_table.getValue(15)


"""
D = intDict(29)
for i in range(20):
    #choose a random int in range(10**5)
    key = random.choice(range(10**5))
    D.addEntry(key, i)

print '\n', 'The buckets are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket
"""















