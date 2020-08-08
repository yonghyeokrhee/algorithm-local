# def solution(paper):
#     arr = np.asarray(paper)
#     total_paper = len(arr)
#     arr_sort = arr.argsort()[::-1]
#     arr_ordered = arr[arr_sort]
#     #citation_sum = np.asarray(paper).sum()
#
#     k = 0
#     for i in np.arange(len(paper))+1:
#         if arr_ordered[:i].sum() > i**2:
#             k += 1
#         else:
#             break
#     #print(k)
#     answer = k
#     return k

# paper = [7,5,8,10,6,9,5]
# solution(paper)

# def solution(n):
#     def factorial(n):
#         if n==0:
#             return 1
#         else:
#             return n*factorial(n-1)
#     facto_num = factorial(n)
#     print(facto_num)
#     i=0
#     strfactonum = str(facto_num)
#     while str(facto_num)[-(i+1)] == '0':
#         i += 1
#     print(i)
#     return i
# solution(20)

import itertools
import numpy as np

def solution(foods):
    food_len = len(foods)
    i = 0
    for itr in itertools.combinations(np.arange(1, food_len), 2):

        pig1 = np.asarray(foods[:itr[0]]).sum()
        pig2 = np.asarray(foods[itr[0]:itr[1]]).sum()
        pig3 = np.asarray(foods[itr[1]:]).sum()


        if pig1 == pig2 == pig3:
            i += 1
        else:
            pass
    print(i)
    answer = i
    return answer


solution([1, 2, 3, 0, 3])
