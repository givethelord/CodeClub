#!/usr/bin/env python

import Queue
import threading
import time

exitFlag = 0


class new_threading(threading.Thread):
    """继承父类threading.Thread"""

    def __init__(self, thread_id, name, queue):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.queue = queue

    def run(self):
        print("start:", self.name)
        # 锁住线程
        threadLock.acquire()
        print_name(self.name, 5, self.queue)
        # 释放线程
        threadLock.release()
        print("exit:", self.name)


def print_name(name, queue):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = queue.get()
            queueLock.release()
            print("%s processing %s" % (name, data))
        else:
            queueLock.release()
    time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]

# 创建线程锁
queueLock = threading.Lock()

# 创建队列
workQueue = Queue.Queue(10)

threads = []
threadID = 1

# 创建新线程
for thread_name in threadList:
    run_thread = new_threading(1, thread_name, workQueue)
    # 开启线程
    run_thread.start()
    # 添加线程到线程列表
    threads.append(run_thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")
