#!/usr/bin/env python3.4

import signal
import time

from handleMessage import handleMessage

def sendMsg(a,b):
  msgHandler(2)

if __name__ == '__main__':
  msgHandler=handleMessage(4)
  signal.signal(signal.SIGCHLD, sendMsg)
  while 1:
    time.sleep(3600)
