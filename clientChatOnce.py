#!/usr/bin/env python3.4
import signal
import time
import sys

def sendMsg(a,b):
  time.sleep(3)
  print('Hi,2V~')
  sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGCHLD, sendMsg)
  while 1:
    time.sleep(3600)