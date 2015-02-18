#!/usr/bin/env python

v = {'a': 1, 'b': 2, 'c': 3, 'arc': 4}


def edit(d):
    d['a'] = 10


print(v)
edit(v)
print(v)

x = filter(lambda k: k.startswith('a'), v)
print(next(x))

print(v.items())