import collections
deq = collections.deque(['a','b','c'])
deq.appendleft('d')
deq.extend('ef')
print(deq)

lst = ['a', 'b', 'c']
lst.extend('d')
print(lst)

lst2 = ['a', 'b', 'c', 'd']
lst2.append('ef') # append()
lst.extend('ef') # extend()

print("lst.extend('ef') >> ", lst)
print("lst2.append('ef') >>", lst2)


