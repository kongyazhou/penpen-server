import os
import time

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()#返回的是子进程的PID
a="哈哈"
if pid == 0:
  while 1:
    print(a)
    a=input()
else:
  while 1:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid) + a)
    time.sleep(2)
