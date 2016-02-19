#!/usr/bin/env python3.4
import sys
from itertools import combinations, count

cases = []
credits = []
items = []

with open(sys.argv[1]) as file_:
    next(file_)
    cases = (list(zip(*[file_]*3)))

for case in cases:
    credits.append(int(case[0]))
    items.append([int(e) for e in case[2].split()])

for credit, prices, i in zip(credits, items, count()):
    for tow_items in combinations(prices, 2):
        if sum(tow_items) == credit:
            print("Case #{}:".format(i+1), end=' ')
            print(' '.join([str(i+1) for i, price in enumerate(prices)
                            if price in tow_items]))
