#!/usr/bin/env python3.4
import sys


def find_two_items_with_sum(list_, sum_):
    hash_ = {}
    for i, element in enumerate(list_, 1):
        if sum_ - element in hash_.keys():
            for t in hash_[sum_ - element]:
                return t, i

        if element in hash_.keys():
            hash_[element].append(i)
        else:
            hash_[element] = [i]

if __name__ == '__main__':
    with open(sys.argv[1]) as file_:
        next(file_)
        for i, case in enumerate(zip(*[file_]*3), 1):
            credit = int(case[0])
            prices = [int(item) for item in case[2].split()]
            tow_items = find_two_items_with_sum(prices, credit)
            print("Case #{}: {} {}".format(i, *tow_items))
