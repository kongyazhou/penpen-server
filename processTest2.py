import os
import time

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()#子进程永远返回0，而父进程返回子进程的ID。
a="哈哈"
if pid == 0:#子进程
  while 1:
    a=input()
    print("child:"+a)  
else:#父进程
  #while 1:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid) + a)
    time.sleep(2)

    #父进程退出会使得子进程异常结束
