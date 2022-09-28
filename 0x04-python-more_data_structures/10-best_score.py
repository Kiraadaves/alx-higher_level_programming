#!/usr/bin/python3
def best_score(a_dictionary):
    v = list(a_dictionary.values())
    max = 0
    if a_dictionary is None or a_dictionary == {}:
        return None
    for i in range(len(v)):
        if v[i] > max:
            max = v[i]
    for x, y in a_dictionary.items():
        if y == max:
            return x
