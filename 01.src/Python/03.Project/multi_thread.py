#!/usr/bin/env python

import threading
import time

exitFlag = 0


class new_threading(threading.Thread):
    """继承父类threading.Thread"""

    def __init__(self, thread_id, name, counter):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("start:", self.name)
        # 锁住线程
        threadLock.acquire()
        print_name(self.name, 5, self.counter)
        # 释放线程
        threadLock.release()
        print("exit:", self.name)


def print_name(name, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print("%s: %s" % (name, time.ctime(time.time())))
        counter -= 1


# 创建线程锁
threadLock = threading.Lock()

threads = []

# 创建新线程
run_thread1 = new_threading(1, "Thread-1", 1)
run_thread2 = new_threading(2, "Thread-2", 2)

# 开启线程
run_thread1.start()
run_thread2.start()

# 添加线程到线程列表
threads.append(run_thread1)
threads.append(run_thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")
