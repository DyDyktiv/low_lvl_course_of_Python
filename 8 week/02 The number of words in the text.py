import sys
import functools


print(len(functools.reduce(set.union,
                           map(lambda line: set(line.split()),
                               sys.stdin))))
