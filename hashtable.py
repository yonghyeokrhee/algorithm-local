# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:59:49 2020
practice hash table John Gutag
@author: joshu
"""
import random

class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary
        which looks like [[],[],[],[],[]]"""
        self.buckets =[]
        self.numBuckets=numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey and int. Adds and entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0]==dictKey:
                hashBucket[i]=(dictKey,dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """Assumes dictKey and int. Returns entry associated with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
            return None
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res+str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}'
            
if __name__ == "__main__":
    D = intDict(29)
    for i in range(20):
        key = random.randint(0, 10**5)
        D.addEntry(key, i)
    print('The value of the intDict is:')
    print(D)
    print('\n', 'The buckets are:')
    for hashBucket in D.buckets:
        print('   ', hashBucket)