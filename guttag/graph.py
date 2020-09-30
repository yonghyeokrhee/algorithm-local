from typing import List


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
    Items = []  # type: List[Item]
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items
