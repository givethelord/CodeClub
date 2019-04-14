#!/usr/bin/env python

from multiprocessing import Process
import time


class new_process(Process):
    """继承父类multiprocessing.process"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):
        print("start:", self.name)
        print("asas", self.arg)
        time.sleep(1)
        print("exit:", self.name)


if __name__ == '__main__':
    for i in range(10):
        p = new_process(i)
        p.start()
