import os
import signal
import time

def getSignal(a,b):
  print("signal.SIGCHLD")

print(os.getpid())
signal.signal(signal.SIGCHLD, getSignal)
while 1:
  time.sleep(100000000000)


