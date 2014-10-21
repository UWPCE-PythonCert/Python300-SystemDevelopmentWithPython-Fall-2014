#!/usr/bin/env python

import argparse
import os
import sys
import urllib2
import multiprocessing
import Queue

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from decorators.decorators import timer

results = multiprocessing.Queue()
url = "http://localhost:37337"

def worker(*args):
    conn = urllib2.urlopen(url)
    result = conn.read()
    conn.close()
    results.put(result)

@timer
def threading_client(number_of_requests=10):
    
    for i in xrange(number_of_requests):
        proc = multiprocessing.Process(target=worker, args=())
        proc.start()
        print "Process %s started" % proc.name

    for i in xrange(number_of_requests):
        print results.get(timeout=1)

    print "made %d requests" % number_of_requests
if __name__ == "__main__":

    number_of_requests = 100
    threading_client(number_of_requests=number_of_requests)
