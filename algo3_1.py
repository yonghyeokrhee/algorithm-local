import itertools
def solution(s):
    string = s
    result = []
    cutoneside = []
    def cutout(string, result):
        if string == '':
            return
        else:
            i = 0
            while string[:i + 1] != string[-(i + 1):]:
                i += 1
            collect = string[:i + 1]
            cutoneside.append(string[i+1:])
            string = string[i + 1:-(i + 1)]
            result.append(collect)
            cutout(string, result)
            print(cutoneside[-1])
        return result,cutoneside

    cutout(string,result)
    if cutoneside[-1] is '':
        for item in itertools.chain(reversed(result)):
            result.append(item)
        del(result[(len(result)//2) - 1])
    else:
        for item in itertools.chain(reversed(result)):
            result.append(item)
    answer = result
    print(answer)
    return answer

solution('abcxyasdfxyabc')