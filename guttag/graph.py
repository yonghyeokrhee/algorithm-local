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

#testGreedys()

def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)

def getBinaryRep(n, numDigits):
    result = ''
    while n> 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

def genPowerSet(L):
    powerSet = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(binStr)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerSet.append(subset)
    return powerSet

def testBest(maxWeight = 20):
    Items = buildItems()
    pset = genPowerSet(Items)
    taken , val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken = ' + str(val))
    for item in taken:
        print(item)

testBest()
