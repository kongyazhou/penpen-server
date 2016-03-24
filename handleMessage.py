#!/usr/bin/env python3.4
import mysql.connector
import json
import os
import base64
import time

class handleMessage(object):
  """
  This module provides all kinds of ways to handle message.
  type: 0 getMessage
        1 recvMessage
        2 readMessage
        3 updateProfile
        4 login#getMsgThenWriteToUsrState
        other error
  """
  def __init__(self,handleType=66):
    self.type=handleType
    if self.type==0:
      self.getMsg()
    elif self.type==1:
      self.recvMsg()
    elif self.type==2:
      self.readMsg()
    elif self.type==3:
      self.updateProfile()
    elif self.type==4:
      self.login()
    else:
      pass
  def __call__(self,handleType=66):
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
    if self.msg["head"]==1100:
      self.msg=self.msg["body"]
    elif self.msg["head"]==1110:
      self.msg=eval(str(base64.b64decode(self.msg["body"]), encoding = "utf-8"))  
    else:
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
  def openMysqlCur(self):
    #创建Mysql cursor
    self.config = {
      'host': 'localhost',
      'port': 3306,
      'database': 'penpen',
      'user': 'root',
      'password': '1',
      'charset': 'utf8',
      'use_unicode': True,
      'get_warnings': True,
    }
    self.cnx = mysql.connector.connect(**self.config)
    self.cur = self.cnx.cursor()
  def closeMysqlCur(self):
    self.cur.close()
    self.cnx.close()
  def sendMsg(self):
    self.codeMsg()
    print(self.msg)    
  def codeMsg(self):
    #将msg编码
    self.codeID=1110
    self.msg={"head":self.codeID,"body":base64.b64encode(self.msg),"tail":"PENPEN 1.0"}
  def readMsg(self):
    """Read message from host's unread table"""
    self.openMysqlCur()
    stmt_select = "SELECT from, to, time, type, content, id FROM %s WHERE unread==1 ORDER BY id" % tuple(self.user)
    self.cur.execute(stmt_select)
    readID=[]
    for row in cur.fetchall():
      self.msg={"from":row[0],"to":row[1],"time":row[2],"type":row[3],"content":row[4]}
      readID.append(((self.user),row[5]))
      self.sendMsg()
    #将未读状态改成已读
    stmt_update = "UPDATE %s SET unread=0 WHERE id=%s"
    self.cur.executemany(stmt_update, tuple(readID))
    cnx.commit()
    slef.closeMysqlCur()
  def recvMsg(self):
    """First get the message, then write it into Mysql."""
    self.getMsg()
    #self.getTarPID()
    #if self.PID:
    self.writeMsg()
      #os.kill(self.PID, signal.SIGCHLD)
    #else:
      #self.pushMsg()
  def writeMsg(self):
    """Write the message to target's unread table"""
    self.openMysqlCur()
    self.getLocalTime()
    stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
     VALUES(%s, %s, '%s', %s, '%s', %d)" % (self.msg["to"],self.msg["from"],self.msg["to"],self.time,self.msg["type"],self.msg["content"],1)
    self.cur.execute(stmt_insert)
    self.closeMysqlCur()
  def getTarPID(self):
    """Get the PID of target from OnlineState database.""" 
    self.openMysqlCur()
    stmt_select = "SELECT online FROM user WHERE user=%s" % (self.msg["to"],)
    self.cur.execute(stmt_select)
    self.tarPID = cur.fetchone()[0]
    self.closeMysqlCur()    
  def pushMsg(self):
    #TODO
    pass
  def login(self):
    self.getMsg()  
    self.user=self.msg["user"]
    if self.checkPassword():
      #print("Login Success.")
      pass 
    else:
      #TODO
      print("Login failed.")
      return
    self.openMysqlCur()
    stmt_update = "UPDATE user SET online=%d WHERE user=%s" % (os.getpid(),self.user)
    self.cur.execute(stmt_update)
    self.closeMysqlCur()
  def checkPassword(self):
    #TODO
    return 1
  def updateProfile(self):
    #TODO
    pass
  def logout(self):
    #TODO
    pass
  def getLocalTime(self):
    self.time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

if __name__ == '__main__':
  a=handleMessage(1)

