from collections import deque
import numpy as np
import random

'''
#True if you can pop one element from left of ordered list and push it to empty list from right in a desired manner
# [1,2,3] --> [3,1,2] False
# [1,2,3] --> [1,3,2] True
'''


def solution(arr):
    answer = []

    def reverse(arr):
        n = len(arr)
        if n == 1:
            return arr
        elif n == 2:
            arr1 = np.array(arr)
            arr2 = arr[::-1]
            return [arr, arr2]
        else:
            for i in range(n-1):
                lefty = arr[:i+1]
                righty = arr[i+1:n]
                print(reverse(lefty))

                answer.append(reverse(lefty)[0])
    reverse(arr)
    return answer


print(solution([1, 3, 2]))
# solution([3,1,2])
