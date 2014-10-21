#!/usr/bin/env python

import threading
import time

x = 1

def func():
    global x
    y = x
    time.sleep(1)
    y += 1
    x = y


threads = []
for x in xrange(100):
    thread = threading.Thread(target=func)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print x
