import time, threading



# 新线程执行的代码:
def loop1(arg):
  a="hoho"
  if arg==1:
    while 1:
      a=input()
      print("1:"+a)
      time.sleep(1)
  else:
    while 1:
      print("2:"+a)
      time.sleep(2)

t1 = threading.Thread(target=loop1, name='LoopThread1',args=(1,))
t2 = threading.Thread(target=loop1, name='LoopThread2',args=(2,))
t1.start()
t2.start()
t2.join()
t1.join()
print('thread %s ended.' % threading.current_thread().name)
