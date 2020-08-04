import math
import numpy as np
import pandas as pd
import itertools


def solution(v):
    if v[0][1] == v[1][1]:
        x = abs(v[0][0] - v[1][0])
    elif v[0][1] == v[2][1]:
        x = abs(v[0][0] - v[2][0])
    elif v[1][1] == v[2][1]:
        x = abs(v[1][0] - v[2][0])

    if v[0][0] == v[1][0]:
        y = abs(v[0][1] - v[1][1])
    elif v[1][0] == v[2][0]:
        y = abs(v[1][1] - v[2][1])
    elif v[0][0] == v[2][0]:
        y = abs(v[0][1] - v[2][1])

    wh = [x, y]

    x = []
    y = []
    for i in v:
        x.append(i[0])
        y.append(i[1])

    x_dict = {}
    for item in x:
        if item in x_dict:
            x_dict[item] += 1
        else:
            x_dict[item] = 1

    y_dict = {}
    for item in y:
        if item in y_dict:
            y_dict[item] += 1
        else:
            y_dict[item] = 1

    answer = []

    for key, value in x_dict.items():
        if value == 1:
            answer.append(key)
    for key, value in y_dict.items():
        if value == 1:
            answer.append(key)
    return answer