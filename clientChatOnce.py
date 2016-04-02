#!/usr/bin/env python3.4
# import signal
import time
import sys
# import base64


def sendMsg(a, b):
    time.sleep(3)
    # msgBody = '{"from":%s,"to":%s,"time":%s,"type":%s,"content":"%s"}' % ("123", "123", "123", "123", "Hello~")
    msg = {"head": 1110,
           "body":
           'encoding="utf-8"',
           "tail":
           "PENPEN 1.0"
           }
    # print(str(base64.b64encode(bytes(msgBody, encoding="utf-8")),encoding="utf-8"))
    print(str(1, encoding="utf-8"))
    # print(bytes(msgBody))
    print(msg)
    sys.exit(0)

if __name__ == '__main__':
    # signal.signal(signal.SIGCHLD, sendMsg)
    sendMsg(1, 2)
    while 1:
        time.sleep(3600)
