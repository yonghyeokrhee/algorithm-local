def solution(input):

    answer_l = [1]
    answer_r = [1]
    num = len(input)
    for i in range(num):

        if i == 0:
            pass
        else:
            cum_l = answer_l[i-1] * input[i-1]
            cum_r = answer_r[i-1] * input[-i]
            answer_l.append(cum_l)
            answer_r.append(cum_r)

    return [i*j for i, j in zip(answer_l,answer_r[::-1])]


if __name__ == '__main__':
    input = [1, 2, 3, 4]
    a = solution(input)
    print(a)