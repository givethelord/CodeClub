#!/usr/bin/env python


class Sample(object):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type:", exc_type)
        print("exc_val:", exc_val)
        print("exc_tb:", exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10


with Sample() as f:
    f.do_something()
