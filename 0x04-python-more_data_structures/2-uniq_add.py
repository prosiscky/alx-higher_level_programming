#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_all = 0
    new_list = list(set(my_list))
    for x in new_list:
        sum_all += x
    return sum_all
