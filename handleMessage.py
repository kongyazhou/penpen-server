#!/usr/bin/env python3.4

import json
import os

class handleMessage(object):
  """
  This module provides all kinds of ways to handle message.
  type: 0 getMessage
        1 receiveMessage
        2 sendMessage
        3 updateProfile
        4 login
        other error
  """
  def __init__(self,handleType=0):
    self.type=handleType
    self.msg=msg
    if self.type==0:
      self.getMsg()
    elif self.type==1:
      self.recvMsg()
    elif self.type==2:
      self.sendMsg()
    elif self.type==3:
      self.sendMsg()
    else:
      pass
  def __call__(self,handleType=0):
    self.__init__(handleType)
  def getMsg(self):
    jsonMsg=input()
    #将json转换成python对象
    self.msg=json.loads(jsonMsg)
    if self.checkVersion():
      pass
    else:
      self.wrongVersion()
    self.decodeMsg()
  def decodeMsg(self):
    """This function decode the package's body part to get the message."""
    #TODO
    if self.msg["head"]==1100:
      self.msg=self.msg["body"]
    elif self.msg["head"]==1110:
      #TODO
      pass
  def checkVersion(self):
    if self.msg["tail"]=="PENPEN 1.0":
      return 1
    else:
      return 0
  def wrongVersion(self):
    #TODO*
    pass
  def sendMsg(self):
    self.readMsgFromUnread()
    self.codeMsg()
    print(self.msg)    
  def codeMsg(self):
    #TODO 将msg编码
    self.codeID=1100
    self.msg={"head":self.codeID,"body":self.msg,"tail":"PENPEN 1.0"}
  def readMsgFromUnread(self):
    """Read message from host's unread table"""
    #TODO
    pass
  def recvMsg(self):
    """First get the message, then write it into Mysql."""
    self.getMsg()
    self.getTarPID()
    if self.PID:
      self.writeMsgToUnread()
      self.sendSignal()
    else:
      self.pushMsg()
  def writeMsgToUnread(self):
    """Write the message to target's unread table"""
    #TODO
    pass
  def getTarPID(self):
    """Get the PID of target from OnlineState database."""
    #TODO 
    self.tarPID=0    
    pass
  def pushMsg(self):
    pass

if __name__ == '__main__':
  print("Message handler!")