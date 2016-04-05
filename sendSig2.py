import os
import signal
import time

pid=input("PID:")
os.kill(int(pid), signal.SIGCHLD)
print("Sended.")




