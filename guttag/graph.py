class Item(object):
    def __init__(self, n , v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', '+str(self.value)\
            +', ' + str(self.weight) + '>'
        return result
    
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def buildItems():
    names = ['clock','painting', 'radio', 'vase', 'book', 'computer']
    vals = [175, 90, 20, 50 , 10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def greedy(Items, maxWeight, keyFcn):
    assert type(Items) == list and maxWeight >=0
    ItemsCopy = sorted(Items, key=keyFcn, reverse=True)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight < maxWeight and i < len(Items):
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append(ItemsCopy[i])
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '   ', item

def testGreedys(maxWeights=20):
    Items = buildItems()
    print 'Use greedy by value for knapsack of size maxWeight'
    testGreedy(Items, maxWeights, value)
    print '\nUse greedy by weight to fill knapsack of size maxWeight'
    testGreedy(Items, maxWeights, weightInverse)
    print '\nUse greedy by density for knapsack of size maxWeight'
    testGreedy(Items, maxWeights, density)

testGreedys()