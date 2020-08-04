def express_n():
    S = [set() for i in range(4)]
    for i,x in enumerate(S, start=1):
        x.add(int(str(N)*i))
    print(S)
    for i in range(1, len(S)):
        for j in range(i):
            for op1 in S[j]:
                for op2 in S[i-j-1]:
                    S[i].add(op1+op2)
                    S[i].add(op1 - op2)
                    S[i].add(op1 * op2)
                    if op2 != 0:
                        S[i].add(op1//op2)

        if number in S[i]:
            answer = i + 1
            break
    print(answer)


N= 2
number =11
express_n()