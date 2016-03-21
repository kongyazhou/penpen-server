import os
import signal
import time

pid=input("PID:")
for x in range(1,10):
  os.kill(int(pid), signal.SIGCHLD)
  print("Sended.")
  time.sleep(1)



