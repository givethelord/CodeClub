#!/usr/bin/env python


def generator(x):
    for i in range(x):
        yield i


print([i + 1 for i in generator(10)])
print([i - 1 for i in generator(10)])
