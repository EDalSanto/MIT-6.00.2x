def powerSet(items):
	"""
	Generates all combinations of N items into one bag, whereby each 
	item is in one or zero bags.
	
	Yields a list that represents the bag
	"""
	N = len(items)
	for i in xrange(2**N):
		combo = []
		for j in xrange(N):
			if (i >> j) % 2 == 1:
				combo.append(items[j])
		yield combo
		
def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        combo = (bag1, bag2)
        for j in xrange(N):
            # test bit jth of integer i
            if (i / (3 ** j)) % 3 == 1: 
                bag1.append(items[j])
            elif (i / (3 ** j)) % 3 == 2:
            	bag2.append(items[j])
        yield combo


items = ['monkey', 'chicken'] 
p = powerSet(items)
s = yieldAllCombos(items)

