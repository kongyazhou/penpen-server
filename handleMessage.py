#!/usr/bin/env python3.4
import jpush as jpush
from conf import app_key, master_secret
import mysql.connector
import json
import os
import base64
import time
import signal
from sys import stdout
from sys import stdin


class handleMessage(object):

    """
    This module provides all kinds of ways to handle message.
    type:
        0       getMessage
        1       readMsg     readMsg from table
        20888   login
        21888   recvMsg
        26888   recvGroupMsg
        31888   updateSigning
        33888   updateState
        51888   syncAllContacts
        53888   syncAllGroups
        60888   createGroup
        other   error
    """

    def __init__(self, handleType=66):
        self.type = handleType
        self._jpush = jpush.JPush(app_key, master_secret)
        self.push = self._jpush.create_push()
        if self.type == 0:
            self.getMsg()
        elif self.type == 1:
            self.readMsg()
        elif self.type == 20888:
            self.login()
        elif self.type == 21888:
            self.recvMsg()
        elif self.type == 26888:
            self.recvGroupMsg()
        elif self.type == 31888:
            self.updateSigning()
        elif self.type == 33888:
            self.updateState()
        elif self.type == 51888:
            self.syncAllContacts()
        elif self.type == 53888:
            self.syncAllGroups()
        elif self.type == 60888:
            self.createGroup()
        else:
            pass

    def __call__(self, handleType=66):
        self.__init__(handleType)

    def getMsg(self):
        jsonMsg = stdin.readline()
        self.msg = json.loads(jsonMsg)
        if self.checkVersion():
            pass
        else:
            self.wrongVersion()
        self.decodeMsg()

    def decodeMsg(self):
        """This function decode the package's body part to get the message."""
        if self.msg["head"] == 1100:
            self.msg = self.msg["body"]
        elif self.msg["head"] == 1110:
            self.msg = eval(str(base64.b64decode(self.msg["body"]), encoding="utf-8"))
        else:
            # TODO
            pass

    def checkVersion(self):
        if self.msg["tail"] == "PENPEN 1.0":
            return 1
        else:
            return 0

    def wrongVersion(self):
        # TODO*
        pass

    def openMysqlCur(self):
        # create Mysql cursor
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
        stdout.flush()

    def codeMsg(self):
        # code msg
        self.codeID = 1110
        self.msg = {"head": self.codeID, "body": str(base64.b64encode(bytes(self.msg, encoding="utf-8")), encoding="utf-8"), "tail": "PENPEN 1.0"}

    def readMsg(self):
        """Read message from host's unread table"""
        self.openMysqlCur()
        stmt_select = "SELECT `from`, `to`, `time`, `type`, `content`, `id` FROM `%s` WHERE unread=1 ORDER BY id" % (self.user,)
        self.cur.execute(stmt_select)
        readID = []
        for row in self.cur.fetchall():
            # TODO If string, take""
            self.msg = '{"from":"%s","to":"%s","time":"%s","type":%d,"content":"%s"}' % (row[0], row[1], row[2], row[3], row[4])
            readID.append((int(self.user), row[5]))
            self.sendMsg()
        # Change unread state to 0
        stmt_update = "UPDATE `%s` SET unread=0 WHERE id=%s"
        self.cur.executemany(stmt_update, tuple(readID))
        self.cnx.commit()
        self.closeMysqlCur()

    def recvMsg(self):
        """First get the message, then write it into Mysql."""
        # TODO check state if online write&send else write&push
        self.getMsg()
        self.getTarPID()
        self.writeMsg()
        if self.tarPID:
            # TOTEST
            os.kill(self.tarPID, signal.SIGCHLD)
            self.pushMsg()
        else:
            self.pushMsg()
            pass

    def recvGroupMsg(self):
        """First get the message, then write it into Mysql."""
        self.getMsg()
        self.groupGID = self.msg["to"]
        # get group members array by gid
        self.getGroupMembers()
        for member in self.groupMembers:
            if member != self.msg["from"]:
                self.msg["to"] = member
                self.getTarPID()
                self.writeGroupMsg()
                if self.tarPID:
                    # TOTEST
                    try:
                        os.kill(self.tarPID, signal.SIGCHLD)
                        self.pushMsg()
                    except:
                        self.pushMsg()
                else:
                    self.pushMsg()
                    pass

    def getGroupMembers(self):
        # TODO
        self.openMysqlCur()
        stmt_select = "SELECT `member` FROM `group` WHERE gid=%s" % (self.groupGID,)
        self.cur.execute(stmt_select)
        self.groupMembers = self.cur.fetchone()[0].split(',')
        self.closeMysqlCur()
        pass

    def writeGroupMsg(self):
        self.openMysqlCur()
        self.getLocalTime()
        stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
            VALUES(%s, '%s', '%s', '%s', '%s', %d)" % (self.msg["to"], self.msg["from"], self.groupGID, self.time, self.msg["type"], self.msg["content"], 1)
        self.cur.execute(stmt_insert)
        self.closeMysqlCur()

    def writeMsg(self):
        """Write the message to target's unread table"""
        self.openMysqlCur()
        self.getLocalTime()
        stmt_insert = "INSERT INTO `%s`( `from`, `to`, `time`, `type`, `content`, `unread`)\
            VALUES('%s', '%s', '%s', '%s', '%s', %d)" % (self.msg["to"], self.msg["from"], self.msg["to"], self.time, self.msg["type"], self.msg["content"], 1)
        self.cur.execute(stmt_insert)
        self.closeMysqlCur()

    def getTarPID(self):
        """Get the PID of target from OnlineState database."""
        self.openMysqlCur()
        stmt_select = "SELECT online FROM user WHERE user=%s" % (self.msg["to"],)
        self.cur.execute(stmt_select)
        self.tarPID = self.cur.fetchone()[0]
        self.closeMysqlCur()

    def pushMsg(self):
        self.push.audience = jpush.audience(jpush.alias("penpen" + self.msg["to"]))
        self.push.notification = jpush.notification(alert=str(base64.b64decode(self.msg["content"]), encoding="utf-8"))
        self.push.platform = jpush.all_
        self.push.send()
        pass

    def login(self):
        self.getMsg()
        self.user = self.msg["user"]
        if self.checkPassword():
            self.loginSuccess()
            pass
        else:
            self.loginFailed()
            return
        self.openMysqlCur()
        stmt_update = "UPDATE user SET online=%d WHERE user=%s" % (os.getpid(), self.user)
        self.cur.execute(stmt_update)
        self.closeMysqlCur()

    def checkPassword(self):
        try:
            self.openMysqlCur()
            stmt_select = "SELECT password FROM user WHERE user=%s" % (self.msg["user"],)
            self.cur.execute(stmt_select)
            self.password = self.cur.fetchone()[0]
        except:
            return False
        else:
            return self.msg["password"] == self.password
        finally:
            self.closeMysqlCur()

    def updateProfile(self):
        # TODO
        pass

    def logout(self):
        # TODO
        pass

    def getLocalTime(self):
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # def createPush(self):
    #     _jpush = jpush.JPush(app_key, master_secret)
    #     self.push = _jpush.create_push()

    def loginSuccess(self):
        self.msg = '{"state":11}'
        self.sendMsg()
        time.sleep(2)
        self.readMsg()

    def loginFailed(self):
        self.msg = '{"state":12}'
        self.sendMsg()

    def syncAllContacts(self):
        self.openMysqlCur()
        self.getDepartments()
        self.getJobs()
        self.getAllContacts()
        self.closeMysqlCur()
        self.msg = str({"departments": self.dictDep, "jobs": self.dictJob, "contacts": self.arrayCon})
        # For test
        # print(self.msg)
        self.sendMsg()

    def syncAllGroups(self):
        self.openMysqlCur()
        stmt_select = "SELECT `gid`, `holder`, `name`, `member` FROM `group`"
        self.cur.execute(stmt_select)
        self.arrayGroup = []
        for row in self.cur.fetchall():
            self.arrayGroup.append({"gid": row[0], "holder": row[1], "name": row[2], "member": row[3]})
        self.closeMysqlCur()
        self.msg = str({"groups": self.arrayGroup})
        # for test
        # print(self.msg)
        self.sendMsg()

    def getDepartments(self):
        stmt_select = "SELECT `id`, `name` FROM `department` ORDER BY id"
        self.cur.execute(stmt_select)
        self.dictDep = {}
        for row in self.cur.fetchall():
            self.dictDep[row[0]] = row[1]

    def getJobs(self):
        stmt_select = "SELECT `id`, `name` FROM `job` ORDER BY id"
        self.cur.execute(stmt_select)
        self.dictJob = {}
        for row in self.cur.fetchall():
            self.dictJob[row[0]] = row[1]

    def getAllContacts(self):
        stmt_select = "SELECT `id`, `name`, `user`, `department`, `job`, `signing` FROM `user` ORDER BY id"
        self.cur.execute(stmt_select)
        self.arrayCon = []
        for row in self.cur.fetchall():
            self.arrayCon.append({"name": row[1], "user": row[2], "department": row[3], "job": row[4], "signing": row[5]})

    def updateState(self):
        self.getMsg()
        self.openMysqlCur()
        stmt_update = "UPDATE user SET state=%d WHERE user=%s" % (self.msg["state"], self.msg["user"])
        self.cur.execute(stmt_update)
        self.closeMysqlCur()

    def updateSigning(self):
        self.getMsg()
        self.openMysqlCur()
        stmt_update = "UPDATE `user` SET `signing`='%s' WHERE `user`=%s" % (self.msg["signing"], self.msg["user"])
        self.cur.execute(stmt_update)
        self.closeMysqlCur()

    def createGroup(self):
        self.getMsg()
        self.openMysqlCur()
        stmt_insert = "INSERT INTO `group`( `holder`,`name`, `member`) VALUES('%s','%s', '%s')" % (self.msg["holder"], self.msg["name"], self.msg["member"])
        self.cur.execute(stmt_insert)
        stmt_select = "SELECT `gid` FROM `group` WHERE `holder`='%s' AND `name`='%s'" % (self.msg["holder"], self.msg["name"])
        self.cur.execute(stmt_select)
        self.groupGID = self.cur.fetchone()[0]
        self.closeMysqlCur()
        # TODO 给member通知
        # get group members array by gid
        self.groupMembers = self.msg["member"].split(',')
        self.group = self.msg
        self.dictContent = {
            "holder": self.group["holder"],
            "name": self.group["name"],
            "member": self.group["member"]
        }
        for member in self.groupMembers:
            self.msg = {
                "from": "0",
                "to": member,
                "type": 19,
                "content": str(base64.b64encode(bytes(str(self.dictContent), encoding="utf-8")), encoding="utf-8")
            }
            self.getTarPID()
            self.writeGroupMsg()
            if self.tarPID:
                try:
                    os.kill(self.tarPID, signal.SIGCHLD)
                except:
                    pass
            else:
                self.pushMsg()
                pass


if __name__ == '__main__':
    a = handleMessage(53888)
