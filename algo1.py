import numpy as np
import pandas as pd
import itertools

lottos, win_nums = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    df = pd.DataFrame({'lottos': lottos, 'win_nums': win_nums})

    min_gotcha = df.lottos.isin(df.win_nums).sum()

    lottos_ar = np.array(lottos)
    lottos_hidden = lottos_ar[[i for i, val in enumerate(lottos) if val == 0]]
    lottos_reveal = lottos_ar[[i for i, val in enumerate(lottos) if val != 0]]

    bowls = np.arange(1, 46)
    possibles = bowls[[i for i, val in enumerate(bowls) if val not in lottos_reveal]]
    possible_combs = np.asarray(list(itertools.combinations(possibles, len(lottos_hidden))))

    luck_combs = []
    for i in possible_combs:
        luck = df.win_nums.isin(i).sum()
        luck_combs.append(luck)

    max_gotcha = max(luck_combs)

    answer = [6 - (max_gotcha+min_gotcha) + 1, 6 - min_gotcha + 1]
    print(answer)
    return answer

solution(lottos, win_nums)