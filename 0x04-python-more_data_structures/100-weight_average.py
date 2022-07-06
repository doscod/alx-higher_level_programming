#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0.0
    score_list = list(t[0] * t[1] for t in my_list)
    weight_list = list(t[1] for t in my_list)
    res = sum(score_list) / sum(weight_list)
    return res
