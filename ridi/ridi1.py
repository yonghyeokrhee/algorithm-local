def solution(arr):
    answer = []
    newarr = list(range(1, len(arr) + 1))
    for i in newarr:
        prefix = newarr[i - 1:]
        suffix = newarr[:i - 1][::-1]
        answer.append(arr == (prefix + suffix))
        #print(prefix + suffix)
    print(bool(sum(answer)))


if __name__ == "__main__":
    arr = [3,2,1,4]
    solution(arr)
