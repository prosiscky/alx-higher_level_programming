#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        for i in range(len(my_list)):
            if i == idx:
                del my_list[i:i+1]
        return my_list
