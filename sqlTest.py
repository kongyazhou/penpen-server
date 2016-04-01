#!/usr/bin/env python3.4
import mysql.connector


class sqlTest(object):
  """docstring for sqlTest"""
  def __init__(self):
    self.user=15669910253    
  def readMsg(self):
    """Read message from host's unread table"""
    self.openMysqlCur()
    # stmt_select = "SELECT from, to, time, type, content, id FROM 15669910253 WHERE unread=1 ORDER BY id" % (self.user,)
    stmt_select = "SELECT `from`, `to`, `time`, `type`, `content`, `id` FROM `%s` WHERE unread=1 ORDER BY id" % (self.user,)
    self.cur.execute(stmt_select)
    # readID=[(15669910253,1),(15669910253,2),(15669910253,3)]
    readID=[]
    for row in self.cur.fetchall():
      #TODO 如果值为字符串，一定要带引号
      self.msg='{"from":%s,"to":%s,"time":%s,"type":%s,"content":"%s"}' % (row[0],row[1],row[2],row[3],row[4])
      print(self.msg)
      readID.append((self.user,row[5]))
      # self.sendMsg()
    #将未读状态改成已读
    stmt_update = "UPDATE `%s` SET unread=0 WHERE id=%s"
    self.cur.executemany(stmt_update, tuple(readID))
    self.cnx.commit()
    self.closeMysqlCur()
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


if __name__ == '__main__':
  a=sqlTest()
  a.readMsg()


