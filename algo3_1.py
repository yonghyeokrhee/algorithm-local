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
            if snip_ind != -1 :
                backward_result.appendleft(s[snip_ind:])
            else:
                pass
            s = s[:snip_ind]
            # recursive function call
            cutoff(s)
            try:
                forward_result.append(backward_result.popleft())
            except IndexError:
                print("No more value left from deque...")
        print(forward_result)
            
        return

    cutoff(s)


solution('abcxyasdfxyabc')
