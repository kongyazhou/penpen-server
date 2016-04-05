#!/usr/bin/env python3.4

from handleMessage import handleMessage
import signal
import time


def onMessage(a, b):
    hm(60888)

if __name__ == '__main__':
    signal.signal(signal.SIGCHLD, onMessage)
    hm = handleMessage(20888)
    while 1:
        time.sleep(3600)
