#!/usr/bin/env python3.4

import json
import os


class sendMessage(object):
  """docstring for ClassName"""
    def __init__(self):
        pass    
    def __call__(self):
        self.getMsg=handleMessage()
        msg=self.getMsg.getUndecodeMessage()
        tarPID=getTargetPID(msg["to"])
        if tarPID!=0:
            self.sendMsg(msg)
        else:
            self.pushMsg(msg)
        
    def sendMsg(self,msg):
        addMsgToTargetMsgtable(msg)
        tarPID=getTargetPID()
        #发送SIGNAL,通知对方进程同步msg
        os.kill(tarPID,??SIGNAL)
    def getTargetPID(self):
        #TODO
        pass
    def addMsgToTargetMsgtable(self,tarID):
        #TODO
        return
    def pushMsg(self,msg):
        pass


if __name__ == '__main__':
    sMsg=sendMessage()
    sMsg()
    

