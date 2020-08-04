import itertools
# def isPalindrome(s):
#
#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#         return ans
#
#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#
#     return isPal(toChars(s))
#
# print(isPalindrome('eve'))

string = 'abcxyasdfasdfxyabc'
result = []

def cutout(string,result):
    if string == '':
        return
    else:
        i = 0
        while string[:i + 1] != string[-(i + 1):]:
            i += 1
        collect = string[:i+1]
        string = string[i + 1:-(i + 1)]
        result.append(collect)
        cutout(string,result)

    return result, reverse


print(cutout(string,result))