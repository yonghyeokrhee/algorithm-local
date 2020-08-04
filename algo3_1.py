import itertools
from collections import deque

def solution(s):

    forward_result = []
    backward_result = deque([])

    def cutoff(s):

        if s == '':
            return
        else:
            i = 0
            while s[:i + 1] != s[-(i + 1):]:
                i += 1
            palindrome = s[:i + 1]
            forward_result.append(palindrome)

            s = s[i+1:]
            snip_ind = s.find(palindrome)
            print(snip_ind)

            backward_result.appendleft(s[snip_ind:])
            s = s[:snip_ind]
            print(forward_result)
            print(backward_result)
            cutoff(s)

            forward_result.append(backward_result.popleft())
            print(forward_result)
        return

    cutoff(s)


solution('abcxyasdfxyabc')