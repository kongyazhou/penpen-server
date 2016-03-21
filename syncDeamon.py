#!/usr/bin/env python3.4

import threading
import os
import signal

from handleMessage import handleMessage

def sendMsg(a,b):
  pass
def login():
  pass

if __name__ == '__main__':
  """Should have two threads, one for send message, another for receive."""
  #login
  msgHandler=handleMessage(4)
  msgHandler()
  deamon=syncDeamon()
  signal.signal(signal.SIGCHLD, sendMsg)
  while 1:
    time.sleep(3600)
