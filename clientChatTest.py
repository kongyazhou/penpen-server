#!/usr/bin/env python3.4
import signal
import time
import sys


def sendMsg(a, b):
    print('Hi,3V~')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGCHLD, sendMsg)
    while 1:
        time.sleep(3600)
