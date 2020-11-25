#!/usr/bin/env python3

import random

def randlist(n, *sets):
    arr = [None] * n
    bucket = set(range(n))
    for i in range(n):
        subset = set(bucket-sets[i])
        if not subset:
            return randlist(n, *sets)
        choice = random.choice(list(subset))
        bucket.remove(choice)
        arr[i] = choice
    return arr

def draw_names(*names):
    actual_names = []
    sets = []
    i = 0
    for name in names:
        if isinstance(name, str):
            actual_names.append(name)
            sets.append({i})
            i += 1
        else:
            sets += [{i, i+len(name)-1}] * len(name)
            actual_names += list(name)
            i += len(name)
    result = randlist(len(actual_names), *sets)
    for index, got_index in enumerate(result):
        print(f'{actual_names[index]} got {actual_names[got_index]}')

if __name__ == "__main__":
    from names import names
    draw_names(*names)
