#!/usr/bin/env python3.4
import sys


with open(sys.argv[1]) as file_:
    next(file_)
    lines = file_.readlines()

for i, line in enumerate(lines):
    print("Case #{}: ".format(i+1), end='')
    print(' '.join(reversed(line.split())))
