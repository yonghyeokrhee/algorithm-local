from collections import deque
import numpy as np
import random

'''
#True if you can pop one element from left of ordered list and push it to empty list from right in a desired manner
# [1,2,3] --> [3,1,2] False
# [1,2,3] --> [1,3,2] True
'''


def solution(arr):
    n = len(arr)
    if n == 1:
        return arr
    elif n == 2:
        arr_r = arr[::-1]
        assert isinstance(arr_r, list)
        return arr, arr_r
    else:
        for i in range(n - 1):
            lefty = arr[:i + 1]
            righty = arr[i + 1:n]

            for left in solution(lefty):
                if isinstance(left, int):
                    for right in solution(righty):
                        print('combine:{}'.format([left]+right))
                else:
                    for right in solution(righty):
                        print('combine:{}'.format(left+[right]))
            # print('combine:{},{}'.format(reverse(righty),reverse(lefty)))
            # answer.append(reverse(lefty)[0])
    return answer


answer = []
solution([1, 2, 3])
# solution([3,1,2])
